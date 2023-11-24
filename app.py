from flask import Flask, request, jsonify, send_file
import cv2 as cv
import numpy as np
import mediapipe as mp
import os
import datetime

app = Flask(__name__)

mp_face_mesh = mp.solutions.face_mesh
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390,
            249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154,
             155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]
LEFT_PUPIL = [473]
RIGHT_PUPIL = [468]


@app.route('/analise', methods=['POST'])
def analyze_image():
    image_file = request.files['image']

    if image_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_path = f"images/{timestamp}.jpg"
        image_file.save(image_path)

        frame = cv.imread(image_path)
        frame_with_timestamp = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        ) as face_mesh:
            frame_with_timestamp = cv.cvtColor(
                frame_with_timestamp, cv.COLOR_RGB2BGR)
            img_h, img_w = frame_with_timestamp.shape[:2]
            results = face_mesh.process(frame_with_timestamp)

            if results.multi_face_landmarks:
                mesh_points = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(
                    int) for p in results.multi_face_landmarks[0].landmark])
                left_iris = mesh_points[LEFT_IRIS]
                right_iris = mesh_points[RIGHT_IRIS]

                left_iris_mean_color = np.mean(
                    frame_with_timestamp[left_iris[:, 1], left_iris[:, 0]], axis=0)
                right_iris_mean_color = np.mean(
                    frame_with_timestamp[right_iris[:, 1], right_iris[:, 0]], axis=0)

                left_pupil_radius = int(np.linalg.norm(
                    mesh_points[LEFT_PUPIL][0] - mesh_points[LEFT_IRIS][0]))
                right_pupil_radius = int(np.linalg.norm(
                    mesh_points[RIGHT_PUPIL][0] - mesh_points[RIGHT_IRIS][0]))

                if not np.array_equal(left_iris_mean_color, [0., 0., 0.]):
                    cv.circle(frame_with_timestamp, tuple(
                        mesh_points[LEFT_PUPIL][0]), left_pupil_radius, (0, 255, 0), 2)

                if not np.array_equal(right_iris_mean_color, [0., 0., 0.]):
                    cv.circle(frame_with_timestamp, tuple(
                        mesh_points[RIGHT_PUPIL][0]), right_pupil_radius, (0, 255, 0), 2)

            resultado = f"{request.host_url}resultado_{timestamp}.jpg"

            cv.imwrite(
                f"results/resultado_{timestamp}.jpg", frame_with_timestamp)
            return jsonify({'result_image': resultado})
    else:
        return jsonify({'error': 'Image not found in request'}), 400


@app.route('/<path:image_name>', methods=['GET'])
def get_analyzed_image(image_name):
    analyzed_image_path = f"results/{image_name}"

    if os.path.exists(analyzed_image_path):
        return send_file(analyzed_image_path, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Image not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
