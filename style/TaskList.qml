import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3


ColumnLayout {
  id: tasks_list_layout
  x: 25
  y: 100
  width: parent.width - 75
  height:  parent.height - y -25

  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}
  TaskWidget {}
  MyTaskSeparator {}

  Rectangle {
    Layout.alignment: Qt.AlignBottom
    Layout.fillHeight: true
    color: Style.myColor5
    Layout.preferredWidth: parent.width
    Layout.preferredHeight: 40
  }


}
