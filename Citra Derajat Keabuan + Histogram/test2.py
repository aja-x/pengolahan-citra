from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *

#https://doc.qt.io/qt-5/qtcharts-datetimeaxis-example.html

if __name__ == '__main__':
    import sys

    a = QApplication(sys.argv)

    x = ['2018-07-01 13:06:38', '2018-07-01 12:46:38', '2018-07-01 12:36:38', '2018-07-01 12:26:38', '2018-07-01 12:16:38', '2018-07-01 12:06:38', '2018-07-01 11:56:38', '2018-07-01 11:46:38', '2018-07-01 11:36:38', '2018-07-01 11:26:38', '2018-07-01 10:56:38', '2018-07-01 10:46:38', '2018-07-01 10:36:38']
    y = [23.5, 20.8, 28.0, 28.1, 28.0, 27.8, 27.3, 27.2, 25.7, 24.7, 25.0, 25.0, 24.9]

    #Chart Type
    series = QLineSeries()
    for t, val in zip(x, y):
        series.append(QDateTime.fromString(t, "yyyy-MM-dd hh:mm:ss").toMSecsSinceEpoch(), val)

    # Create Chart and set General Chart setting
    chart = QChart()
    chart.addSeries(series)
    chart.setTitle("Temperature records in celcius")
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # X Axis Settings
    axisX = QDateTimeAxis()
    axisX.setTickCount(10)
    axisX.setFormat("dd HH mm") #https://doc.qt.io/qt-5/qdatetime.html#toString-2
    axisX.setTitleText("Day")
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Y Axis Settings
    axisY = QValueAxis()
    axisY.setLabelFormat("%i")
    axisY.setTitleText("Temperature C")
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Create a QChartView object with QChart as a parameter. This way we don't need to create the QGraphicsView scene ourselves. We also set the Antialiasing on to have the rendered lines look nicer.
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    chart.axisY(series).setRange(min(y)-5, max(y)+5)
    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)
    window = QMainWindow()
    window.setCentralWidget(chartView)
    window.resize(1280, 480)
    window.show()
    sys.exit(a.exec_())