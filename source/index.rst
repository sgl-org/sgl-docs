.. SGL documentation master file, created by
   sphinx-quickstart on Sat Mar 30 21:31:33 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SGL's documentation!
===============================

.. image:: SGL_logo.png

SGL(Small Graphics Library)是一个非常轻量的GUI图形库，其设计的初衷就是针对低端处理器市场提供一个现代化的图形框架。代码仓库：\ `SGL on GitHub <https://github.com/sgl-org/sgl>`_
SGL官方技术交流群QQ：544602724，欢迎大家加入！！！
   
SGL UI库特点:

- 轻量级，最小只需要 ``3KBytes RAM`` 和 ``15KBytes ROM`` 即可运行
- 部分帧缓冲支持，最小只需要一行屏幕分辨率的缓冲即可
- 包围盒 + 贪心算法的脏矩形算法
- 支持帧缓冲控制器，直接向帧缓冲控制器写入数据，零拷贝
- 颜色深度支持: ``8bit``, ``16bit``, ``24bit``, ``32bit``
- 现代化的字体取模工具
- ``SGL`` 自己的 ``UI`` 设计器，图形化拖动绘制界面后一键可生成代码

.. toctree::
   :maxdepth: 2
   :caption: 目录:

   docs/000-start.md
   docs/001-base.md
   docs/file_system.md
   docs/000-2dball.md
   docs/002-fontgen.md
   docs/003-pixmapgen.md
   docs/004-button.md
   docs/005-label.md
   docs/006-led.md
   docs/007-switch.md
   docs/008-img.md
   docs/009-msgbox.md
   docs/010-line.md
   docs/011-canvas.md
   docs/012-barchart.md
   docs/013-arc.md
   docs/014-bar.md
   docs/015-box.md
   docs/016-checkbox.md
   docs/017-circle.md
   docs/018-dropdown.md
   docs/019-icon.md
   docs/020-imgtool.md
   docs/021-progress.md
   docs/022-ring.md
   docs/023-slider.md
   docs/024-textbox.md
   docs/025-textline.md
   docs/026-textlist.md
   docs/027-viewlist.md
   docs/028-win.md
   docs/029-keyboard.md
   docs/030-linechart.md
   docs/031-piechart.md
   docs/032-numberkbd.md
   docs/033-polygon.md
   docs/034-qrcode.md
   docs/035-rectangle.md
   docs/036-scope.md
   docs/037-scroll.md
   docs/039-unzipimage.md

QQ交流群
==================
.. image:: qqgroup.png
   :width: 300px

捐款
==================
SGL完全免费开源，可以用于商用，如果觉得对你有帮助，可以给SGL团队捐赠，所有捐款将用于SGL项目的开发和维护，谢谢！      

.. image:: alipay.png
   :width: 300px
