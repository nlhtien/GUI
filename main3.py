import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot, QTimer
from PyQt5.QtGui import QTextCursor
from pyqtgraph import PlotWidget, mkPen
from PyQt5.QtWidgets import QTimeEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from ahrs.filters import Madgwick
import ahrs
from GUI3 import Ui_MainWindow
import socket
import threading
import numpy as np
import math
from pyqtgraph import PlotWidget, mkPen
from scipy.spatial.transform import Rotation
from scipy.signal import find_peaks
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pyqtgraph as pg
from scipy.optimize import curve_fit



def read_data_from_file(filename):
    # Đọc dữ liệu từ file
    AX_values, AY_values, AZ_values = [], [], []
    WX_values, WY_values, WZ_values = [], [], []
    MX_values, MY_values, MZ_values = [], [], []


    with open(filename, 'r') as file:
        for line in file:
            values = [float(s.split(':')[1]) for s in line.strip().split(', ')]
            AX, AY, AZ, WX, WY, WZ, MX, MY, MZ = values
            AX_values.append(AX)
            AY_values.append(AY)
            AZ_values.append(AZ)
            WX_values.append(WX)
            WY_values.append(WY)
            WZ_values.append(WZ)
            MX_values.append(MX)
            MY_values.append(MY)
            MZ_values.append(MZ)

    return AX_values, AY_values, AZ_values, WX_values, WY_values, WZ_values, MX_values, MY_values, MZ_values

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        # Set default IP and port
        self.textEdit_ip.setPlainText("192.168.230.138")
        self.textEdit_port.setPlainText("12345")

        # Connect buttons to functions
        self.btn_send.clicked.connect(self.connect_to_server)
        self.btn_send_2.clicked.connect(self.disconnect_from_server)
        self.btn_send_5.clicked.connect(self.save_data)
        self.btn_send_6.clicked.connect(self.plot_data)
        self.btn_send_3.clicked.connect(self.clear_data)
        self.btn_send_4.clicked.connect(self.import_data)
        self.btn_send_7.clicked.connect(self.start_disconnect_timer)



        # Set up socket variables
        self.server_address = None
        self.server_port = None
        self.socket = None
        self.receive_data_timer = QTimer()
        self.receive_data_timer.timeout.connect(self.receive_data_timer_func)

        # Khởi tạo 9 list để lưu giữ giá trị của từng vị trí
        self.AX_values, self.AY_values, self.AZ_values = [], [], []
        self.AX_values2, self.AY_values2, self.AZ_values2 = [], [], []
        self.WX_values, self.WY_values, self.WZ_values = [], [], []
        self.WX_values2, self.WY_values2, self.WZ_values2 = [], [], []
        self.MX_values, self.MY_values, self.MZ_values = [], [], []
        self.MX_values2, self.MY_values2, self.MZ_values2 = [], [], []
        self.Roll_values, self.Pitch_values, self.Yaw_values = [], [], []
        self.Roll_values2, self.Pitch_values2, self.Yaw_values2, self.Yaw2_values2 = [], [], [], []
        self.Roll_values3, self.Pitch_values3, self.Yaw_values3, self.Yaw2_values3 = [], [], [], []



        # Flag để theo dõi trạng thái kết nối
        self.connected = False

        # Số điểm dữ liệu trên đồ thị
        self.num_data_points = 100
        self.num_data_points2 = 420
        self.init_plot_objects()
        # Set default values for timeEdit
        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # Thêm khai báo disconnect_time
        self.disconnect_time = None



        # Khởi tạo giá trị x cho đồ thị
        self.x_values = list(range(1, self.num_data_points + 1))
        self.y_values = list(range(1, self.num_data_points2 + 1))


        # Khởi tạo các đối tượng plot
        self.init_plot_objects()

    @pyqtSlot()
    def start_disconnect_timer(self):
        # Start the timer to disconnect based on the selected time in timeEdit
        self.disconnect_time = self.timeEdit.time()
        self.receive_data_timer.start(1000)  # Start the data receiving timer
        self.show_message_box("Info", "Disconnect timer started. Will disconnect at the specified time.")
        print(f"Disconnect time set to: {self.disconnect_time}")

    def init_plot_objects(self):
        # Initialize a list to store plot data
        self.data_series = []

        # Set colors for the plots
        colors = ['r', 'g', 'b']
        for i in range(13):
            pen_color = colors[i % 3]
            pen = mkPen(color=pen_color, width=1)
            plot_item = getattr(self, f"myplot_{i + 1}")
            data_series = plot_item.plot(pen=pen, symbol='o', symbolSize=1)
            self.data_series.append(data_series)

    @pyqtSlot()
    def connect_to_server(self):
        if self.connected:
            self.show_message_box("Error", "Already connected to the server.")
            return

        ip_text = self.textEdit_ip.toPlainText()
        port_text = self.textEdit_port.toPlainText()

        try:
            self.server_port = int(port_text)
        except ValueError:
            self.show_message_box("Error", "Invalid port number.")
            return

        self.server_address = ip_text

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address, self.server_port))
            self.connected = True
            self.receive_data_timer.start(1000)  # Cập nhật mỗi 1000 ms (1 giây)
            self.show_message_box("Success", "Connected to the server.")
            self.textBrowser_tb4.append("Connected to the server.")

        except Exception as e:
            self.show_message_box("Error", f"Failed to connect to the server: {str(e)}")

    @pyqtSlot()
    def disconnect_from_server(self):
        if self.socket is not None:
            self.socket.close()
            self.socket = None
            self.connected = False
            self.receive_data_timer.stop()
            self.show_message_box("Success", "Disconnected from the server.")
            self.textBrowser_tb4.append("Disconnected from the server.")
            self.display_disconnect_status()

        else:
            self.show_message_box("Error", "Not connected to the server.")

    @pyqtSlot()
    def receive_data_timer_func(self):
        try:
            data = self.socket.recv(1024)
            if not data:
                return

            # Check if the disconnect time is set
            if self.disconnect_time is not None:
                # Check if the current time is greater than or equal to the specified disconnect time
                current_time = QtCore.QTime.currentTime()
                if current_time >= self.disconnect_time and self.connected:
                    self.disconnect_from_server()
                    print(
                        f"Current time: {current_time}, Disconnect time: {self.disconnect_time}, Connected: {self.connected}")
            # Assuming data is a string; modify as per your data format
            data_str = data.decode("utf-8")


            # Tách giá trị từ chuỗi dữ liệu
            values = {key: float(value) for key, value in (item.split(":") for item in data_str.split(', '))}

            # Lưu dữ liệu vào file
            self.save_data_to_file(data_str)

            # Hiển thị giá trị từng vị trí lên textBrowser_tb3 và xóa nội dung cũ
            self.display_values_on_tb3(values)
            # Cập nhật đồ thị
            self.update_plot_data(values)





        except Exception as e:
            print(f"Error receiving data: {str(e)}")


    def display_values_on_tb3(self, values):
        # Xóa nội dung cũ
        self.clear_text_browser_tb3()

        tb3_content = f"AX: {values['AX']}, AY: {values['AY']}, AZ: {values['AZ']}\n"
        tb3_content += f"WX: {values['WX']}, WY: {values['WY']}, WZ: {values['WZ']}\n"
        tb3_content += f"MX: {values['MX']}, MY: {values['MY']}, MZ: {values['MZ']}\n"

        cursor = self.textBrowser_tb3.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(tb3_content)
        self.textBrowser_tb3.setTextCursor(cursor)
        self.textBrowser_tb3.ensureCursorVisible()

    # Thêm một phương thức để xóa nội dung của textBrowser_tb3
    def clear_text_browser_tb3(self):
        self.textBrowser_tb3.clear()

    def save_data_to_file(self, data):
        # Save data to a file
        with open("data_log.txt", "a") as file:
            file.write(data + "\n")

        # Limit the file to 30 lines
        with open("data_log.txt", "r") as file:
            lines = file.readlines()
            if len(lines) > 500:
                with open("data_log.txt", "w") as file:
                    file.writelines(lines[-500:])

    @pyqtSlot()
    def save_data(self):
        # Implement save data logic here
        pass

    @pyqtSlot()
    def plot_data(self):
        # Implement plot data logic here
        pass

    @pyqtSlot()
    def update_plot_data(self, values=None):
        if values is None:
            # Đọc dữ liệu từ file khi không có dữ liệu được cung cấp
            self.AX_values, self.AY_values, self.AZ_values, self.WX_values, self.WY_values, self.WZ_values, \
                self.MX_values, self.MY_values, self.MZ_values = read_data_from_file("data_log.txt")
        else:
            # Cập nhật giá trị mới vào biến giữ liệu
            data_list = [
                self.AX_values,
                self.AY_values,
                self.AZ_values,
                self.WX_values,
                self.WY_values,
                self.WZ_values,
                self.MX_values,
                self.MY_values,
                self.MZ_values,
            ]
            for i, key in enumerate(values.keys()):
                data_list[i].append(values[key])
                data_list[i] = data_list[i][-self.num_data_points:]

            # Ensure that the lengths of data lists are at least num_data_points
            for i in range(9):
                while len(data_list[i]) < self.num_data_points:
                    data_list[i].insert(0, 0.0)  # You can change 0.0 to any default value

            # Scale dữ liệu để nhận thấy rõ sự thay đổi
            scaled_data = np.array(data_list) * 1

            # Cập nhật dữ liệu đồ thị
            for i in range(9):
                self.data_series[i].setData(self.x_values[-len(data_list[i]):], scaled_data[i])

            # Calculate roll, pitch, and yaw from sensor data
            acc_data = np.array([self.AX_values[-1], self.AY_values[-1], self.AZ_values[-1]])
            gyro_data = np.array([self.WX_values[-1], self.WY_values[-1], self.WZ_values[-1]])
            mag_data = np.array([self.MX_values[-1], self.MY_values[-1], self.MZ_values[-1]])

            # Complementary filter parameters
            alpha = 0.98
            yaw_gyro = 0.0
            dt = 1.0  # Assuming a constant time interval for simplicity

            # Gyro calibration
            gyro_data_calibrated = self.gyro_calibration(gyro_data)
            # Append the calibrated gyro data to the list
            self.WX_values2.append(gyro_data_calibrated[0])
            self.WY_values2.append(gyro_data_calibrated[1])
            self.WZ_values2.append(gyro_data_calibrated[2])

            acc_data_calibrated = self.accel_calibration()
            # Append the calibrated acc data to the list
            self.AX_values2.append(acc_data_calibrated[0])
            self.AY_values2.append(acc_data_calibrated[1])
            self.AZ_values2.append(acc_data_calibrated[2])

            mag_offsets, mag_gains = self.mag_calib()
            # Append the calibrated mag data to the list
            # Apply calibration to current magnetometer values
            MX_calibrated = (self.MX_values[-1] - mag_offsets[0]) * mag_gains[0]
            MY_calibrated = (self.MY_values[-1] - mag_offsets[1]) * mag_gains[1]
            MZ_calibrated = (self.MZ_values[-1] - mag_offsets[2]) * mag_gains[2]
            #print(f"mag {MX_calibrated} {MY_calibrated} {MZ_calibrated}")



            # Append the calibrated values to the lists
            self.MX_values2.append(MX_calibrated)
            self.MY_values2.append(MY_calibrated)
            self.MZ_values2.append(MZ_calibrated)


            acc_data /= np.linalg.norm(acc_data)
            mag_data /= np.linalg.norm(mag_data)

            roll_pitch_yaw = Rotation.from_matrix([gyro_data, acc_data, mag_data])
            rpy = roll_pitch_yaw.as_euler('xyz', degrees=True)
            # if(rpy[0]<0):
            #     rpy[0]=-rpy[0];
            # Lưu giá trị roll, pitch, yaw vào danh sách
            self.Roll_values.append(rpy[0])
            self.Pitch_values.append(rpy[1])
            self.Yaw_values.append(rpy[2])

            # Giới hạn số lượng phần tử trong các mảng về 65 và xóa giá trị ở vị trí 0 khi có giá trị mới
            max_elements = 420
            self.Roll_values = self.Roll_values[-max_elements:]
            self.Pitch_values = self.Pitch_values[-max_elements:]
            self.Yaw_values = self.Yaw_values[-max_elements:]

            # Cập nhật dữ liệu đồ thị cho roll, pitch, yaw
            self.data_series[9].setData(self.y_values[-len(self.Roll_values):], self.Roll_values)
            self.data_series[10].setData(self.y_values[-len(self.Pitch_values):], self.Pitch_values)
            self.data_series[11].setData(self.y_values[-len(self.Yaw_values):], self.Yaw_values)

            # Giới hạn số lượng phần tử trong các mảng về 65 và xóa giá trị ở vị trí 0 khi có giá trị mới
            max_elements2 = 120
            self.WX_values2 = self.WX_values2[-max_elements2:]
            self.WY_values2 = self.WY_values2[-max_elements2:]
            self.WZ_values2 = self.WZ_values2[-max_elements2:]

            # plot gyro
            self.hrz = np.arange(120)  # abscissa
            pen1 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
            pen2 = pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.SolidLine)
            pen3 = pg.mkPen(color=(0, 200, 0), width=2, style=QtCore.Qt.SolidLine)

            self.myplot_13.plot(self.hrz[:len(self.WX_values2)], self.WX_values2, name="wx", pen=pen1, clear=True)
            self.myplot_13.plot(self.hrz[:len(self.WX_values2)], self.WY_values2, name="wy", pen=pen2, clear=False)
            self.myplot_13.plot(self.hrz[:len(self.WX_values2)], self.WZ_values2, name="wz", pen=pen3, clear=False)

            print(f"gyro {gyro_data_calibrated[0]} {gyro_data_calibrated[1]} {gyro_data_calibrated[2]}")

            # Giới hạn số lượng phần tử trong các mảng về 65 và xóa giá trị ở vị trí 0 khi có giá trị mới
            self.AX_values2 = self.AX_values2[-max_elements2:]
            self.AY_values2 = self.AY_values2[-max_elements2:]
            self.AZ_values2 = self.AZ_values2[-max_elements2:]

            # # Tăng khoảng trục y cho myplot_14
            # self.myplot_15.setRange(yRange=[-1, 1])
            #
            # # Tăng khoảng trục y cho myplot_15
            # self.myplot_14.setRange(yRange=[-2.3e-12, -2e-12])

            # plot gyro
            self.hrz = np.arange(120)  # abscissa
            pen1 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
            pen2 = pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.SolidLine)
            pen3 = pg.mkPen(color=(0, 200, 0), width=2, style=QtCore.Qt.SolidLine)

            self.myplot_14.plot(self.hrz[:len(self.AX_values2)], self.AX_values2, name="ax", pen=pen1, clear=True)
            self.myplot_14.plot(self.hrz[:len(self.AY_values2)], self.AY_values2, name="ay", pen=pen2, clear=False)
            self.myplot_14.plot(self.hrz[:len(self.AZ_values2)], self.AZ_values2, name="az", pen=pen3, clear=False)

            print(f"acc {acc_data_calibrated[0]} {acc_data_calibrated[1]} {acc_data_calibrated[2]}")

            # Limit the number of elements in the lists
            max_elements = 120
            self.MX_values2 = self.MX_values2[-max_elements:]
            self.MY_values2 = self.MY_values2[-max_elements:]
            self.MZ_values2 = self.MZ_values2[-max_elements:]



            self.hrz = np.arange(120)  # abscissa
            pen1 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
            pen2 = pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.SolidLine)
            pen3 = pg.mkPen(color=(0, 200, 0), width=2, style=QtCore.Qt.SolidLine)

            # Update the plot for calibrated magnetometer values
            self.myplot_15.plot(self.hrz[:len(self.MX_values2)], self.MX_values2, name="ax", pen=pen1, clear=True)
            self.myplot_15.plot(self.hrz[:len(self.MY_values2)], self.MY_values2, name="ay", pen=pen2, clear=False)
            self.myplot_15.plot(self.hrz[:len(self.MZ_values2)], self.MZ_values2, name="az", pen=pen3, clear=False)

            print(f"mag {MX_calibrated} {MY_calibrated} {MZ_calibrated}")

            # RPY CALIB
            acc_data2 = np.array([acc_data_calibrated[0],acc_data_calibrated[1],acc_data_calibrated[2]])
            #acc_data2 = acc_data
            gyro_data2 = np.array([gyro_data_calibrated[0], gyro_data_calibrated[1], gyro_data_calibrated[2]])
            mag_data2 = np.array([MX_calibrated,MY_calibrated,MZ_calibrated])

            YAW = self.mahony_filter(gyro_data2,acc_data,mag_data2)



            #acc_data2 /= np.linalg.norm(acc_data2)
            #mag_data2 /= np.linalg.norm(mag_data2)

            roll_pitch_yaw2 = Rotation.from_matrix([gyro_data2, acc_data2, mag_data2])
            rpy2 = roll_pitch_yaw2.as_euler('xyz', degrees=True)
            roll, pitch, yaw, yaw_gyro = self.complementary_filter(acc_data, gyro_data2, dt, alpha, yaw_gyro)

            max_elements3 = 10
            self.Roll_values3 = self.Roll_values3[-max_elements3:]
            self.Pitch_values3 = self.Pitch_values3[-max_elements3:]
            self.Yaw_values3 = self.Yaw_values3[-max_elements3:]
            self.Yaw2_values3 = self.Yaw2_values3[-max_elements3:]

            self.Roll_values3.append(roll)
            self.Pitch_values3.append(pitch)
            self.Yaw_values3.append(yaw)
            self.Yaw2_values3.append(YAW)

            # Tính trung bình của mỗi mảng
            average_roll = np.mean(self.Roll_values3)
            average_pitch = np.mean(self.Pitch_values3)
            average_yaw = np.mean(self.Yaw_values3)

            # if(rpy[0]<0):
            #     rpy[0]=-rpy[0];



            # Lưu giá trị roll, pitch, yaw vào danh sách
            self.Roll_values2.append(average_roll*180/3.14)
            self.Pitch_values2.append(average_pitch*180/3.14)
            self.Yaw_values2.append(average_yaw*180/3.14)
            self.Yaw2_values2.append(YAW)


            # print(f"rpy {rpy2[0]} {rpy2[1]} {rpy2[2]}")
            # print(f"rpy avg {average_roll} {average_pitch} {average_yaw}")


            # Giới hạn số lượng phần tử trong các mảng về 65 và xóa giá trị ở vị trí 0 khi có giá trị mới
            max_elements = 400
            self.Roll_values2 = self.Roll_values2[-max_elements:]
            self.Pitch_values2 = self.Pitch_values2[-max_elements:]
            self.Yaw_values2 = self.Yaw_values2[-max_elements:]
            self.Yaw2_values2 = self.Yaw2_values2[-max_elements:]


            self.hrz = np.arange(400)  # abscissa
            pen1 = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.SolidLine)
            pen2 = pg.mkPen(color=(0, 0, 255), width=2, style=QtCore.Qt.SolidLine)
            pen3 = pg.mkPen(color=(0, 200, 0), width=2, style=QtCore.Qt.SolidLine)

            # Update the plot for calibrated magnetometer values
            self.myplot_17.plot(self.hrz[:len(self.Roll_values2)], self.Roll_values2, name="ax", pen=pen1, clear=True)
            self.myplot_18.plot(self.hrz[:len(self.Pitch_values2)], self.Pitch_values2, name="ay", pen=pen2, clear=True)
            self.myplot_19.plot(self.hrz[:len(self.Yaw_values2)], self.Yaw2_values2, name="az", pen=pen3, clear=True)
            #self.myplot_19.plot(self.hrz[:len(self.Yaw2_values2)], self.Yaw2_values2, name="az2", pen=pen1, clear=False)

            madgwick = Madgwick(gain=0.033)  # You can adjust the gain as needed
            Q = np.array([1.0, 0.0, 0.0, 0.0])  # Initialize Q with identity quaternion
            Q = madgwick.updateMARG(Q, gyr=gyro_data2, acc=acc_data2,  mag=mag_data2)
            g2d = ahrs.common.RAD2DEG
            ypr = ahrs.common.orientation.q2euler(Q) * g2d  # rad to degree
            ypr2 = self.quaternion_to_euler_angle(Q[0], Q[1], Q[2], Q[3])

            print('{}'.format('-' * 30))
            print('accel [m/s^2]:   x = {0:2.2f},   y = {1:2.2f},   z = {2:2.2f} '.format(acc_data2[0], acc_data2[1],
                                                                                          acc_data2[2]))
            print('gyro [gps]:  x = {0:2.2f},   y = {1:2.2f},   z = {2:2.2f}'.format(gyro_data2[0], gyro_data2[1],
                                                                                     gyro_data2[2]))
            print('mag [mT]:    x = {0:2.2f},   y = {1:2.2f},   z = {2:2.2f}'.format(mag_data2[0], mag_data2[1],
                                                                                     mag_data2[2]))
            print('euler:   yaw = {0:2.2f},   pitch = {1:2.2f},   roll = {2:2.2f} '.format(ypr[0], ypr[1], ypr[2]))
            print('{}'.format('-' * 30))
            print('euler2:   yaw = {0:2.2f},   pitch = {1:2.2f},   roll = {2:2.2f} '.format(ypr2[0], ypr2[1], ypr2[2]))
            print('{}'.format('-' * 30))
            print('euler3:   yaw = {0:2.2f},   pitch = {1:2.2f},   roll = {2:2.2f} '.format(rpy2[2], rpy2[1], rpy2[0]))
            print('{}'.format('-' * 30))
            print('euler4:   yaw = {0:2.2f},   pitch = {1:2.2f},   yaw2 = {2:2.2f}'.format(average_yaw*180/3.14, average_pitch*180/3.14, average_yaw*180/3.14))
            print('{}'.format('-' * 30))
            print('euler5:   yaw = {0:2.2f},   pitch = {1:2.2f},   yaw2 = {2:2.2f}'.format(YAW,1,1))
            print('{}'.format('-' * 30))
            # Move the cursor to the end of textBrowser_tb3
            cursor = self.textBrowser_tb3.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.textBrowser_tb3.setTextCursor(cursor)
            self.textBrowser_tb3.ensureCursorVisible()

            # Chú ý dòng này để cập nhật đồ thị
            QApplication.processEvents()

    def accel_fit(self, x_input, m_x, b):
        return (m_x * x_input) + b  # fit equation for accel calibration

    def mahony_filter(self,gyro_data, accel_data, mag_data):
        global angle, gyro_bias
        ax, ay, az = accel_data
        gx, gy, gz = gyro_data
        mx, my, mz = mag_data

        # Tham số cho bộ lọc Mahony
        sampleFreq = 100.0  # Tần số lấy mẫu (Hz)
        beta = 0.1  # Hệ số bộ lọc
        dt = 1/sampleFreq

        # Biến toàn cục
        angle = 0.0
        gyro_bias = [0.0, 0.0, 0.0]

        q0, q1, q2, q3 = 1.0, 0.0, 0.0, 0.0

        # Thực hiện bước dự đoán
        qDot1 = 0.5 * (-q1 * gx - q2 * gy - q3 * gz)
        qDot2 = 0.5 * (q0 * gx + q2 * gz - q3 * gy)
        qDot3 = 0.5 * (q0 * gy - q1 * gz + q3 * gx)
        qDot4 = 0.5 * (q0 * gz + q1 * gy - q2 * gx)

        # Hợp nhất dữ liệu từ cảm biến
        recipNorm = 1.0 / math.sqrt(ax * ax + ay * ay + az * az + mx * mx + my * my + mz * mz)
        ax *= recipNorm
        ay *= recipNorm
        az *= recipNorm
        mx *= recipNorm
        my *= recipNorm
        mz *= recipNorm

        s0 = 2.0 * (q0 * q2 + q1 * q3)
        s1 = q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3
        s2 = -2.0 * (q0 * q1 - q2 * q3)
        s3 = 2.0 * (q1 * q2 + q0 * q3)

        s4 = q1 * q3 - q0 * q2
        s5 = q0 * q1 + q2 * q3
        s6 = q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3

        # Gradient descent để điều chỉnh ước lượng góc
        qDot1 -= beta * s0
        qDot2 -= beta * s1
        qDot3 -= beta * s2
        qDot4 -= beta * s3

        # Tích hợp giá trị đạo hàm để có ước lượng góc mới
        q0 += qDot1 * dt
        q1 += qDot2 * dt
        q2 += qDot3 * dt
        q3 += qDot4 * dt

        # Chuẩn hóa vectơ quaternion
        recipNorm = 1.0 / math.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        q0 *= recipNorm
        q1 *= recipNorm
        q2 *= recipNorm
        q3 *= recipNorm

        # Chuyển đổi quaternion sang góc Euler
        angle = math.atan2(2.0 * (q1 * q2 + q0 * q3), q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3) * (180.0 / math.pi)

        # Tính toán sai số của con quay hồi chuyển
        gyro_bias[0] += 2.0 * beta * s4 * dt
        gyro_bias[1] += 2.0 * beta * s5 * dt
        gyro_bias[2] += 2.0 * beta * s6 * dt
        return angle
    def quaternion_to_euler_angle(self,w, x, y, z):
        ysqr = y * y

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + ysqr)
        roll_x = math.degrees(math.atan2(t0, t1))
        roll_x = roll_x * 180 / (3.14)  # rad->degree

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.degrees(math.asin(t2))
        pitch_y = pitch_y * 180 / (3.14)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (ysqr + z * z)
        yaw_z = math.degrees(math.atan2(t3, t4))
        yaw_z = yaw_z * 180 / (3.14)

        return roll_x, pitch_y, yaw_z


    def mag_calib(self,data_log_filename="data_log.txt"):
        # Đọc dữ liệu từ file
        AX_values, AY_values, AZ_values, WX_values, WY_values, WZ_values, MX_values, MY_values, MZ_values = read_data_from_file(
            data_log_filename)

        cal_size = 500;

        # Lấy 100 giá trị gần nhất từ MX, MY, MZ
        MX_values_recent = MX_values[-cal_size:]
        MY_values_recent = MY_values[-cal_size:]
        MZ_values_recent = MZ_values[-cal_size:]

        mag_data_recent = np.array([MX_values_recent, MY_values_recent, MZ_values_recent])

        mag_offsets = [0.0, 0.0, 0.0]
        mag_gains = [0.0, 0.0, 0.0]
        mx_max = np.nanmax(mag_data_recent[:, 0])
        mx_min = np.nanmin(mag_data_recent[:, 0])
        my_max = np.nanmax(mag_data_recent[:, 1])
        my_min = np.nanmin(mag_data_recent[:, 1])
        mz_max = np.nanmax(mag_data_recent[:, 2])
        mz_min = np.nanmin(mag_data_recent[:, 2])

        mag_offsets[0] = (mx_max + mx_min) / 2
        mag_offsets[1] = (my_max + my_min) / 2
        mag_offsets[2] = (mz_max + mz_min) / 2

        epsilon = 1e-10  # Một giá trị nhỏ để tránh lỗi chia cho không

        mag_gains[0] = 1 / (mx_max - mx_min + epsilon)
        mag_gains[1] = 1 / (my_max - my_min + epsilon)
        mag_gains[2] = 1 / (mz_max - mz_min + epsilon)

        return mag_offsets, mag_gains

    def complementary_filter(self,accel_data, gyro_data, dt, alpha, yaw_gyro):
        ax, ay, az = accel_data
        wx, wy, wz = gyro_data

        # Roll and Pitch from accelerometer
        roll = np.arctan2(ay, az)
        pitch = np.arctan2(-ax, np.sqrt(ay ** 2 + az ** 2))

        # Yaw from gyroscope
        yaw_gyro += wz * dt

        # Complementary filter for Yaw
        yaw_comp = alpha * yaw_gyro + (1 - alpha) * np.arctan2(ay, ax)

        return roll, pitch, yaw_comp, yaw_gyro
    def accel_calibration(self):
        acc_calib = [0, 0, 0]  # Slope array to be printed
        axis_vec = ['z', 'y', 'x']  # Axis labels
        cal_size = 500

        for qq, ax_qq in enumerate(axis_vec):
            ax_offsets = []

            # Đọc dữ liệu từ file khi không có dữ liệu được cung cấp
            # Lấy 100 giá trị gần nhất từ AX, AY, AZ
            AX_values_recent = self.AX_values[-cal_size:]
            AY_values_recent = self.AY_values[-cal_size:]
            AZ_values_recent = self.AZ_values[-cal_size:]
            if ax_qq == 'x':
                ax_offsets = np.array(AX_values_recent)
            elif ax_qq == 'y':
                ax_offsets = np.array(AY_values_recent)
            elif ax_qq == 'z':
                ax_offsets = np.array(AZ_values_recent)


            # Use three calibrations (+1g, -1g, 0g) for linear fit
            input_data = np.concatenate([1.0 * np.ones(np.shape(ax_offsets)),
                                         -1.0 * np.ones(np.shape(ax_offsets)),
                                         0.0 * np.ones(np.shape(ax_offsets))])
            output_data = np.concatenate([ax_offsets, ax_offsets, ax_offsets])

            try:
                # Fit a linear equation ax + b
                popts, _ = curve_fit(self.accel_fit, input_data, output_data, maxfev=10000, p0=[1.0, 0.0])
                acc_calib[qq] = popts[0]  # Store the slope (m) in the array
            except Exception as e:
                print(f"Error in curve_fit: {str(e)}")

        return acc_calib

    def gyro_calibration(self, gyro_data):
        # Calculate mean offset for each axis

        mean_offsets = np.mean(np.array([self.WX_values[-500:], self.WY_values[-500:], self.WZ_values[-500:]]), axis=1)
        #print(f"wx {self.WX_values}")
        # Calibrate gyro data by subtracting mean offsets
        calibrated_data = gyro_data - mean_offsets
        return calibrated_data
    @pyqtSlot()
    def clear_data(self):
        # Xóa nội dung của textBrowser_tb3
        self.clear_text_browser_tb3()
        self.clear_text_browser_tb2()
        self.clear_text_browser_tb()
        self.textBrowser_tb4.append("clear all \n")

    @pyqtSlot()
    def import_data(self):
        # Implement import data logic here
        pass
    def display_disconnect_status(self):
        # Display connect/disconnect status on textBrowser_tb4
        status_message = "Connected" if self.connected else "Disconnected"
        self.textBrowser_tb4.clear()
        self.textBrowser_tb4.append(status_message)
    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
