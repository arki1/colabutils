

def list_faces(faces,
               likelihoods=('joy', 'surprise', 'sorrow',
                            'anger', 'under exposed', 'blurred'),
               likelihoods_responses=('unknown', 'NO, very unlikely', 'NO, unlikely',
                            'MAYBE', 'YES, likely', 'YES, very likely')):
  if len(faces) == 0:
    print('no face found!')
    return

  facenum = 1
  for face in faces:
    print('FACE #{}'.format(facenum))
    print('  confidence: {}'.format(face.detection_confidence*100))
    print('  {}: {} ({})'.format(likelihoods[0],
                                 likelihoods_responses[face.joy_likelihood], face.joy_likelihood))
    print('  {}: {} ({})'.format(likelihoods[1],
                                 likelihoods_responses[face.surprise_likelihood], face.surprise_likelihood))
    print('  {}: {} ({})'.format(likelihoods[2],
                                 likelihoods_responses[face.sorrow_likelihood], face.sorrow_likelihood))
    print('  {}: {} ({})'.format(likelihoods[3],
                                 likelihoods_responses[face.anger_likelihood], face.anger_likelihood))
    print('  {}: {} ({})'.format(likelihoods[4],
                                 likelihoods_responses[face.under_exposed_likelihood], face.under_exposed_likelihood))
    print('  {}: {} ({})'.format(likelihoods[5],
                                 likelihoods_responses[face.blurred_likelihood], face.blurred_likelihood))
    print('')
    facenum += 1


def list_annotations(annotations):
  if len(annotations) == 0:
    print('no text found!')
  else:
    print('\n'.join([d.description for d in annotations]))


def list_labels(labels):
  if len(labels) == 0:
    print('no label found!')
  else:
    print('\n'.join(['{} ({})'.format(d.description, d.score*100) for d in labels]))
