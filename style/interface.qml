import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3



ApplicationWindow {
  id: root_window
  width: 600
  height: 600
  flags: Qt.Window | Qt.FramelessWindowHint
  visible: true
  title: qsTr("PitToDo")
  color: "transparent"
  // moving window
  MouseArea {
    anchors.fill: parent
    property variant clickPos: "1,1"
    onPressed: {
        clickPos  = Qt.point(mouse.x,mouse.y)
    }
    onPositionChanged: {
        var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y)
        root_window.x += delta.x;
        root_window.y += delta.y;
    }
  }

  Rectangle {
    radius: 15
    color: Style.myColor5
    border.color: Style.myColor1
    border.width: 5
    anchors.fill: parent
    anchors.centerIn: parent

    TopBar {}
    TaskList {}
    // TaskWidget {}

    Image {
      source: "../images/logo.png"
      x: 25
      y: 25
    }
  }


}
