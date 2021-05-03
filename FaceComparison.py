import face_recognition


first_image = input('Enter the path of your reference image:')
second_image = input('Enter the path of the image you want to compare:')


image = face_recognition.load_image_file('images/' + first_image)
face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

second_image = face_recognition.load_image_file('images/' + second_image)
face_locations = face_recognition.face_locations(second_image)
face_landmarks_list = face_recognition.face_landmarks(second_image)


biden_encoding = face_recognition.face_encodings(image)[0]
unknown_encoding = face_recognition.face_encodings(second_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

result = "Not same person"

if results[0] == True:
    result = "Same person"

print(result)

exit()
