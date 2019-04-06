from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import io

def record(auto_play=False):
  js = Javascript('''
    async function recordAudio(autoPlay) {
      const div = document.createElement('div');
      const startButton = document.createElement('button');
      startButton.textContent = 'Start Recording';
      div.appendChild(startButton);
      
      const cancelButton = document.createElement('button');
      cancelButton.textContent = 'Cancel';
      div.appendChild(cancelButton);
      
      // Resize the output to fit the audio element.
      google.colab.output.setIframeHeight(50, true);
      
      const finishButton = document.createElement('button');
      finishButton.textContent = 'Finish';
      
      cancelButton.style.marginLeft = '5px';
      finishButton.style.marginLeft = '5px';

      document.body.appendChild(div);

      var recording, stream, blobURL, blobDataURL, promiseResolve;
      var audioChunks = [];

      // when start button is clicked, starts recording and enables save
      startButton.onclick = async function () {
        startButton.disabled = true;

        div.appendChild(finishButton);

        const audio = document.createElement('audio');
        audio.style.display = 'block';
        audio.style.paddingTop = '10px';
        div.appendChild(audio);

        stream = await navigator.mediaDevices.getUserMedia({audio: true});
        recording = new MediaRecorder(stream);
        recording.ondataavailable = (e) => {
          audioChunks.push(e.data);
          
          if (recording.state == "inactive") {
            const blob = new Blob(audioChunks);
            blobURL = URL.createObjectURL(blob);
            audio.src = blobURL;
            audio.controls = true;
            if (autoPlay) audio.autoplay = autoPlay;
            var fileReader = new FileReader();
            fileReader.onload = function(e) {
              blobDataURL = e.target.result;
              if (promiseResolve) promiseResolve();
            };   
            fileReader.readAsDataURL(blob);
          }
        };
        recording.start();
      };
      
      var stopRecording = function() {
        // stop recording
        if ((recording) && (recording.stop)) recording.stop();

        // stop all tracks
        if ((stream) && (stream.getTracks)) stream.getTracks().forEach( track => track.stop() );     
      };
      
      finishButton.onclick = stopRecording;

      // wait for a button to be clicked.
      var finishClicked = await new Promise(async function(resolve, reject) {
        cancelButton.onclick = resolve;
        promiseResolve = resolve;
      });
      
      startButton.disabled = true;
      finishButton.disabled = true;
      cancelButton.disabled = true;

      return blobDataURL;
    }
    ''')
  display(js)
  auto_play_str = "true" if auto_play else "false"
  data = eval_js('recordAudio({})'.format(auto_play_str))
  if (data is None or data == ''):
    return None
  return b64decode(data.split(',')[1])

def record_and_save(filename='audio.wav', auto_play=False):
  content = record(auto_play)
  if content is None:
    return None

  with open(filename, 'wb') as f:
    f.write(content)

  return filename
