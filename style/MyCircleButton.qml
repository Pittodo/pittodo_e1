import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3



Button {
  id: btn_status
  text: qsTr("CB")

  onClicked: console.log("Button "+ text +" clicked!")

  contentItem: Text {
    text: parent.text
    font: parent.font
    horizontalAlignment: Text.AlignHCenter
    verticalAlignment: Text.AlignVCenter
  }
  background: Rectangle {
    height: 30
    width: height
    radius: height/2
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    color: parent.down ? Style.myColor2 : Style.myColor1
  }

}
