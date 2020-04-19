import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3


ColumnLayout {
  id: tasks
  x: 25
  y: 100
  width: parent.width - 75
  height:  parent.height - y -25


  RowLayout {
    height: 40
    Rectangle {
      Layout.preferredHeight: control.height
      color: "magenta"

      MouseArea {
        anchors.fill: parent
        onClicked: console.log("Rectangle outer clicked")
      }
      TextArea {
        x:0
        y:0
        id: control
        placeholderText: qsTr("Enter new task...")
        color: Style.myColor1

        background: Rectangle {
          implicitWidth: 200
          // implicitHeight: 30
          // color: control.hovered ? Style.myColor1 : "transparent"
          color: control.enabled ? "transparent" : "#353637"
          border.color: control.enabled ? "#21be2b" : "transparent"
        }
      }
    }
  }
  Rectangle {
    Layout.alignment: Qt.AlignBottom
    Layout.fillHeight: true
    color: "pink"
    Layout.preferredWidth: parent.width
    Layout.preferredHeight: 40
  }


}
