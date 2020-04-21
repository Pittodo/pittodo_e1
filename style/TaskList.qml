import QtQuick 2.0
import "." // QTBUG-34418, singletons require explicit import to load qmldir file
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Flickable {
  // Layout.fillHeight: true
  // Layout.fillWidth: true
  id: flickable
  x: 15
  y: 100
  width: root_window.width - 45
  height:  root_window.height - y -25

  contentHeight: contentItem.childrenRect.height
  // contentWidth: width
  clip: true

  boundsBehavior: Flickable.StopAtBounds
  flickableDirection: Flickable.VerticalFlick

  ColumnLayout {
    id: tasks_list_layout

    MyTaskSeparator {}
    TaskWidget {}
    MyTaskSeparator {}
    TaskWidget {}


    // Rectangle {
    //   Layout.alignment: Qt.AlignBottom
    //   // Layout.fillWidth: true
    //   color: Style.myColor1
    //   Layout.preferredWidth: parent.width
    //   Layout.preferredHeight: 50
    // }
  }
  ScrollBar.vertical: ScrollBar {
    id: vscroll
    policy: ScrollBar.AsNeeded
    parent: flickable.parent
    anchors.top: flickable.top
    anchors.left: flickable.right
    anchors.bottom: flickable.bottom

    contentItem: Rectangle {
      implicitWidth: 6
      implicitHeight: 100
      radius: width / 2
      color: vscroll.pressed ? Style.myColor2 : Style.myColor1
    }
  }
}
