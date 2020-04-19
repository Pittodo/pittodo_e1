import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file


Rectangle {
  x: 0
  y: 0
  width: parent.width
  height: 40
  radius: parent.radius
  color: "transparent"

  Rectangle {
    y: 25
    height: 30
    width: 30
    radius: 15
    x: parent.width - 25 - width
    color: Style.myColor1

    MouseArea {
      anchors.fill: parent
      onClicked: console.log("Button exit clicked!")
    }
  }
  Rectangle {
    y: 25
    height: 30
    width: 30
    radius: 15
    x: parent.width - 60 - width
    color: Style.myColor1

    MouseArea {
      anchors.fill: parent
      onClicked: console.log("Button minimize clicked!")
    }
  }
}
