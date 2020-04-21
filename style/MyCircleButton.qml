import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3



Button {
  id: btn_status
  text: qsTr("CB")
  onClicked: console.log("Button "+ text +" clicked!")
  height: 30
  width: height

  contentItem: Text {
    text: parent.text
    font: parent.font
    color: Style.myColor5
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
  }
  background: Rectangle {
    height: btn_status.height-5
    width: height
    radius: height/2
    // border.width: 5
    // border.color: "transparent"
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    color: btn_status.down ? Style.myColor2 : Style.myColor1
  }

}
