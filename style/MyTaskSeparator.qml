import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ToolSeparator {
  orientation: Qt.Horizontal
  Layout.alignment: Qt.AlignHCenter
  Layout.fillWidth: true

  contentItem: Rectangle{
    implicitWidth: 300
    implicitHeight: 2
    radius: 1
    color: Style.myColor4
    MouseArea {
      anchors.fill: parent
      cursorShape: Qt.PointingHandCursor
      hoverEnabled: true
      onEntered: { parent.color = Style.myColor1 }
      onExited: { parent.color = Style.myColor4 }
      onWheel: {}
    }
    MyCircleButton {
      background.height: 20
      y: -background.height/2
      x: parent.width/2 - background.height/2
      text: "+"
    }

  }

}
