本节将指导你如何在不同的平台上移植SGL图形库

## SGL移植步骤

### PC模拟器

1. 安装make工具，确保make命令可用    

2. 安装MinGW工具链，确保gcc命令可用，这里推荐一个gcc工具链地址：[MinGW 13.2.0 工具链](https://github.com/niXman/mingw-builds-binaries/releases/download/13.2.0-rt_v11-rev0/x86_64-13.2.0-release-posix-seh-ucrt-rt_v11-rev0.7z)

3. 安装git工具，确保git命令可用        

4. 安装git工具后，打开git命令行，依次输入如下命令，即可完成SGL的移植：      
   
   ```bash
       git clone https://github.com/sgl-org/sgl-port-windows.git
       cd sgl-port-windows
       git submodule init
       git submodule update --remote
       cd demo
       make -j8
       make run
   ```

5. 执行完毕后，即可看到一个窗口，显示SGL的示例程序运行效果        
   
   ```{tip}
   如果想修改模拟器的分辨率，可以在`sgl_port_sdl2.c`文件中修改`CONFIG_SGL_PANEL_WIDTH`和`CONFIG_SGL_PANEL_HEIGHT`的值
   ```

### MCU平台

1. 建议下载SGLmain[最新代码压缩包](https://github.com/sgl-org/sgl/archive/refs/heads/main.zip)

2. 解压后如下文件结构：
   
   ```textile
   source
   ├─sgl.h                     SGL统一头文件
   ├─sgl_config.h              SGL配置文件
   ├─build.cmake               CMake构建配置
   ├─lm.cfg                    模块构建配置
   ├─components                可选功能组件
   │  ├─3dvortex               3D动画组件
   │  └─timer                  软件定时器组件
   ├─core                      SGL核心
   ├─draw                      底层图形绘制库
   ├─fonts                     字体资源
   ├─include                   头文件
   ├─fs                        文件系统抽象与适配
   │  ├─fatfs                  FatFS适配层
   │  ├─littlefs               LittleFS适配层
   │  └─ramfs                  内存文件系统
   ├─mm                        内存管理
   │  ├─bump                   Bump线性分配器
   │  ├─lwmem                  lwmem内存管理器
   │  ├─other                  自定义内存管理接口
   │  ├─tiny
   │  └─tlsf                   TLSF内存管理器
   └─widgets                   控件
      ├─2dball                 2D小球
      ├─analogclock            模拟指针时钟
      ├─arc                    一段圆弧
      ├─arc_label              可旋转弧形标签
      ├─bar                    可交互填充条
      ├─battery                电池状态图标
      ├─box                    可滚动容器
      ├─button                 按钮
      ├─canvas                 自定义画布
      ├─chart                  图表控件
      │  ├─barchart            柱状图
      │  ├─linechart           折线图
      │  └─piechart            饼图/环形图
      ├─checkbox               复选框
      ├─circle                 圆形
      ├─dropdown               下拉选择框
      ├─filebrowser            文件浏览器
      ├─gauge                  指针式仪表盘
      ├─icon                   单色图标
      ├─img                    图片/RLE/多帧图片
      ├─img_ext                可旋转缩放的图片
      ├─keyboard               全键盘
      ├─label                  普通文字标签
      ├─label_ext              可旋转扩展标签
      ├─launcher               多页应用菜单启动器
      ├─led                    LED灯
      ├─line                   线段
      ├─msgbox                 消息对话框
      ├─numberkbd              数字键盘
      ├─polygon                多边形
      ├─progress               进度条
      ├─qrcode                 二维码
      ├─rectangle              矩形容器
      ├─ring                   圆环
      ├─roller                 滚轮选择器
      ├─scope                  多通道波形图
      ├─scroll                 滚动条
      ├─slider                 滑动杆
      ├─spectrum               频谱图
      ├─sprite                 ARGB4444游戏精灵
      ├─statusbar              状态栏
      ├─switch                 开关
      ├─textbox                可滚动文本框
      ├─textline               自动换行文本框
      ├─textlist               纯文字列表容器
      ├─unzip_image            配合文件系统显示压缩图片
      ├─viewlist               可滑动的列表容器
      └─win                    带标题栏的窗口
   ```

3. 将SGL的所有代码拷贝到MCU的工程文件中，并添加所有文件，注意：对于mm目录下的文件，只需要添加lwmem目录下的文件，如果你的项目中已经有动态内存管理函数，则不需要添加mm目录下的文件，自己定义`sgl_mm_init`，`sgl_malloc`，`sgl_free`函数即可。

4. 将sgl源码的sgl.h文件所在的目录添加到编译的头文件路径中

5. 将sgl源码的include目录添加到编译的头文件中路径中

6. 添加SGL的所有文件后，请修改`sgl_config.h`文件，用于适配你的MCU平台，下面是一个示例：

```c
#ifndef  __CONFIG_H__
#define  __CONFIG_H__

#define    CONFIG_SGL_FBDEV_PIXEL_DEPTH       16          //颜色深度，这里是16位，即RGB565
#define    CONFIG_SGL_FBDEV_ROTATION          0           //屏幕旋转角度，软件旋转，这里设置为0度，即不做旋转
#define    CONFIG_SGL_FBDEV_RUNTIME_ROTATION  0           //屏幕实时旋转角度
#define    CONFIG_SGL_SYSTICK_MS              10          //SGL图形刷新事件间隔，这里设置为10ms
#define    CONFIG_SGL_EVENT_QUEUE_SIZE        16          //事件队列大小，这里设置为16
#define    CONFIG_SGL_DIRTY_AREA_NUM_MAX      16          //脏区域最大数量，这里设置为16
#define    CONFIG_SGL_ANIMATION               1           //是否启用动画，这里启用动画
#define    CONFIG_SGL_DEBUG                   1           //是否启用日志，这里启用日志，项目发布时，请关闭日志
#define    CONFIG_SGL_LOG_COLOR               1           //是否启用日志颜色，这里启用日志颜色
#define    CONFIG_SGL_LOG_LEVEL               0           //日志等级，0为全部输出，1为错误输出，2为警告输出，3为信息输出，4为调试输出
#define    CONFIG_SGL_OBJ_USE_NAME            0           //是否启用对象名称，这里不启用对象名称
#define    CONFIG_SGL_FONT_COMPRESSED         1           //是否启用字体压缩，这里启用字体压缩
#define    CONFIG_SGL_BOOT_LOGO               1           ///是否启用启动logo，这里启用开机logo
#define    CONFIG_SGL_HEAP_ALGO               lwmem       //内存管理算法，这里选择lwmem
#define    CONFIG_SGL_HEAP_MEMORY_SIZE        10240       //内存大小，这里设置为10KB
#define    CONFIG_SGL_FONT_SONG23             0           //是否启用宋体23号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS14         0           //是否启用Consolas14号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS23         0           //是否启用Consolas23号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS24         1           //是否启用Consolas24号字体, 默认开启
#define    CONFIG_SGL_FONT_CONSOLAS32         0           //是否启用Consolas32号字体, 默认关闭
#define    CONFIG_SGL_FONT_CONSOLAS24_COMPRESS     1      //是否启用Consolas24号字体压缩，这里启用字体压缩

#endif  //!__CONFIG_H__
```

```{tip}
开发阶段，最好开启`CONFIG_SGL_DEBUG`，这样可以使用串口输出调试日志，如果出现问题，可以快速定位原因。
```

7. 对接屏幕底层驱动代码
   在你的main函数中添加如下代码：

```c
#include "sgl.h"
#define PANEL_WIDTH     320
#define PANEL_HEIGHT    240

static sgl_color_t panel_buffer[PANEL_WIDTH * 10];

void panel_flush_area(sgl_area_t *area, sgl_color_t *src)
{
    uint16_t w = area->x2 - area->x1 + 1;
    uint16_t h = area->y2 - area->y1 + 1;
    tft_set_win(area->x1, area->y1, area->x2, area->y2);
    GPIO_WriteBit(SPI_DC_PORT, SPI_DC_PIN, 1);
    /*阻塞式刷新函数*/
    SPI1_WriteMultByte((uint8_t*)src, w * h * sizeof(sgl_color_t));
    /* 调用sgl_fbdev_flush_ready()函数，告诉SGL框架，刷新完成，可以继续处理下一帧处理 */ 
    sgl_fbdev_flush_ready();
}

void uart_put_string(const char *str)
{
   /* 发送串口数据，将str中的数据发送出去 */
}

//你的SysTick中断处理函数，定时时间为1ms
void SysTick_Handler(void)
{
    sgl_tick_inc(1);
}

int main(void)
{
    sgl_fbinfo_t fbinfo = {
        .xres = PANEL_WIDTH,
        .yres = PANEL_HEIGHT,
        .flush_area = panel_flush_area,
        .buffer[0] = panel_buffer,
        .buffer_size = SGL_ARRAY_SIZE(panel_buffer), 
    };

    // 注册日志设备，可选
    sgl_logdev_register(uart_put_string);
    // 注册Framebuffer设备
    sgl_fbdev_register(&fbinfo);

    // 必须先初始化SysTick和屏幕设备，然后再初始化SGL框架
    systick_init();
    tft_init();

    sgl_init();

    //添加一个测试代码
    sgl_obj_t *label = sgl_label_create(NULL);
    sgl_obj_set_size(label, PANEL_WIDTH, 30);
    sgl_obj_set_pos_align(label, SGL_ALIGN_CENTER);
    sgl_label_set_font(label, &consolas24);
    sgl_label_set_text(label, "Hello SGL!");

    while(true){
        sgl_task_handler();
    }
    return 0;

}
```

上面的过程中定义了一个`sgl_fbinfo_t`结构体，并且初始化了一些主要的参数，参数的含义如下： 

- `xres`: 屏幕的宽度          
- `yres`: 屏幕的高度                
- `flush_area`：刷新区域函数，用于刷新指定区域           
- `buffer[0]`：帧缓冲区指针，指向帧缓冲区地址处，如何需要双帧缓冲区，则需要设置`buffer[1]`        
- `buffer_size`：帧缓冲区大小，单位：缓冲区中像素点的个数          

`panel_flush_area`函数用于刷新指定区域，参数为：

- `area`：区域结构体指针，包含区域左上角和右下角的坐标
    `x1`：区域左上角X坐标
    `y1`：区域左上角Y坐标
    `x2`：区域右下角X坐标
    `y2`：区域右下角Y坐标
- `src`：区域数据指针
  如果不使用DMA刷新，`panel_flush_area`函数必须调用`sgl_fbdev_flush_ready()`函数，用来告诉SGL框架，刷新完成，可以继续处理下一帧处理。

当然，对于使用DMA发送数据时，请使用双缓冲，即添加一个缓冲区，即`buffer[1]`，大小和`buffer[0]`一样，即`buffer_size`

```c
//DMA完成回调函数
void dma_complete_cb(void)
{
    sgl_fbdev_flush_ready();
}

void panel_flush_area(sgl_area_t *area, sgl_color_t *src)          
{
    // 非阻塞模式
    DMA_SendData_NoWait(src, (x2 - x1 + 1) * (y2 - y1 + 1)* sizeof(sgl_color_t));
}
```

编译后，烧录到开发板上，即可看到屏幕显示“Hello SGL!”，整个移植主要只有四件事：    

- 1. 调用sgl_fbdev_register()函数注册FB设备      
- 2. 调用sgl_logdev_register()函数注册日志设备，可选        
- 3. 调用sgl_init()函数初始化SGL框架       
- 4. 在滴答中断中调用sgl_tick_inc()函数，定时为1ms    

```{danger}
sgl_tick_inc()所在的Systick或者定时器必须在SGL初始化之前就应该被初始化，否则会导致启动LOGO进入卡死状态，sgl_tick_inc()函数不是必须要在滴答中断中调用，你也可以在轮询或者线程中调用，保证每1ms调用一次即可。
```

### KEIL IDE使用

#### 以下keil[移植教程](https://www.bilibili.com/video/BV1ezxNzHEeV/)也可点击在B站观看

#### 1.创建工程

1. 新建一个`SGL_STM32F103`目录，然后创建一个`sgl`目录，然后将`sgl`源码的`source`目录下的所有文件复制到`SGL_STM32F103/sgl/`目录下。      
    ![alt text](imgs/mdk5/image-1.png)

2. 打开`MDK5`软件，新建一个名为`SGL_STM32F103`的工程，保存到`SGL_STM32F103`目录下，点击【保存】。      
    ![alt text](imgs/mdk5/img-2.jpg)

3. 此时会进入芯片选择界面，然后选择STM32F103C8芯片，点击【OK】      
    ![alt text](imgs/mdk5/img-3.jpg)

4. 此时会进入`Manage Run-Time Environment`界面，勾选`CMSIS`和`Startup`，然后点击【OK】。       
    ![alt text](imgs/mdk5/img-4.jpg)

5. 点击文件扩展管理器:      
    ![alt text](imgs/mdk5/img-5.jpg)
   
    然后新建`sgl`和`example`目录结构，然后在`sgl`结构中，将`sgl/core/`目录下所有c文件添加，将`sgl/draw/`目录下所有c文件添加，将`sgl/fonts/`目录下所有c文件添加，将`sgl/source/mm/lwmem/`目录下的所有c文件添加，将`sgl/source/widgets/`目录下的所有文件添加，添加完毕后，目录结构如下：           
    ![alt text](imgs/mdk5/img-6.jpg)

6. 新建一个`main.c`文件，然后保存到`example`文件夹下：            
    ![alt text](imgs/mdk5/img-7.jpg)
   
    然后输入如下代码：          
   
   ```c
   #include "stm32f10x.h"
   #include "sgl.h"
   
   #define  PANEL_WIDTH    240
   #define  PANEL_HEIGHT   240
   sgl_color_t panel_buffer[PANEL_WIDTH * 10];
   
   /* 系统时钟中断服务函数，设置为1ms中断一次 */
   void systick_handler(void){
       sgl_tick_inc(1);
   }
   
   void panel_flush_area(sgl_area_t *area, sgl_color_t *src)
   {
       /*以下两个函数需自行适配屏幕*/
       tft_set_win(area->x1, area->y1, area->x2, area->y2);    
       SPI1_WriteMultByte((uint8_t*)src, (area->x2 - area->x1 + 1) * (area->y2 - area->y1 + 1) * sizeof(sgl_color_t));
       /* 调用sgl_fbdev_flush_ready()函数，通知SGL刷新完成，可以继续处理下一帧处理 */ 
       sgl_fbdev_flush_ready();
   }
   /*可自行实现输出日志功能*/
   void UART1_SendString(const char *str)
   {
       while (*str != '\0') {
           while ((USART1->SR & USART_SR_TXE) == 0);
           USART1->DR = (uint8_t)(*str++);
       }
       while ((USART1->SR & USART_SR_TC) == 0);
   }
   
   int main(void)
   {
       sgl_fbinfo_t fbinfo = {
           .xres = PANEL_WIDTH,
           .yres = PANEL_HEIGHT,
           .flush_area = panel_flush_area,
           .buffer[0] = panel_buffer,
           .buffer_size = SGL_ARRAY_SIZE(panel_buffer), 
       };
       // 注册日志设备，可选
       sgl_logdev_register(UART1_SendString);
       // 注册Framebuffer设备
       sgl_fbdev_register(&fbinfo);
   
       // 必须先初始化SysTick和屏幕设备，然后再初始化SGL框架
       uart_init();
       systick_init();
       tft_init();
   
       /* init sgl */
       sgl_init();
   
       while(1){
           sgl_task_handler();
       }
   
       return 0;
   }
   ```

7. 编辑`sgl_config.h`文件，修改内容如下：
   
   ```c
   #define    CONFIG_SGL_FBDEV_PIXEL_DEPTH       16          //颜色深度，这里是16位，即RGB565
   #define    CONFIG_SGL_FBDEV_ROTATION          0           //屏幕旋转角度，软件旋转，这里设置为0度，即不做旋转
   #define    CONFIG_SGL_FBDEV_RUNTIME_ROTATION  0           //屏幕实时旋转角度
   #define    CONFIG_SGL_SYSTICK_MS              10          //SGL图形刷新事件间隔，这里设置为10ms
   #define    CONFIG_SGL_EVENT_QUEUE_SIZE        16          //事件队列大小，这里设置为16
   #define    CONFIG_SGL_DIRTY_AREA_NUM_MAX      16          //脏区域最大数量，这里设置为16
   #define    CONFIG_SGL_ANIMATION               1           //是否启用动画，这里启用动画
   #define    CONFIG_SGL_DEBUG                   1           //是否启用日志，这里启用日志，项目发布时，请关闭日志
   #define    CONFIG_SGL_LOG_COLOR               1           //是否启用日志颜色，这里启用日志颜色
   #define    CONFIG_SGL_LOG_LEVEL               0           //日志等级，0为全部输出，1为错误输出，2为警告输出，3为信息输出，4为调试输出
   #define    CONFIG_SGL_OBJ_USE_NAME            0           //是否启用对象名称，这里不启用对象名称
   #define    CONFIG_SGL_FONT_COMPRESSED         1           //是否启用字体压缩，这里启用字体压缩
   #define    CONFIG_SGL_BOOT_LOGO               1           ///是否启用启动logo，这里不启用启动logo
   #define    CONFIG_SGL_HEAP_ALGO               lwmem       //内存管理算法，这里选择lwmem
   #define    CONFIG_SGL_HEAP_MEMORY_SIZE        10240       //内存大小，这里设置为10KB
   #define    CONFIG_SGL_FONT_SONG23             0           //是否启用宋体23号字体, 默认关闭
   #define    CONFIG_SGL_FONT_CONSOLAS14         0           //是否启用Consolas14号字体, 默认关闭
   #define    CONFIG_SGL_FONT_CONSOLAS23         0           //是否启用Consolas23号字体, 默认关闭
   #define    CONFIG_SGL_FONT_CONSOLAS24         1           //是否启用Consolas24号字体, 默认开启
   #define    CONFIG_SGL_FONT_CONSOLAS32         0           //是否启用Consolas32号字体, 默认关闭
   #define    CONFIG_SGL_FONT_CONSOLAS24_COMPRESS     1      //是否启用Consolas24号字体压缩，这里启用字体压缩
   ```
   
   #### 2.配置编译选项

8. 打开`Options for Target`窗口，然后找到`Target`选项:             
    ![alt text](imgs/mdk5/img-8.jpg)
   
    选择`V6`版本编译器

9. 点击`C/C++(AC6)`选项`，然后选择如下配置：              
    ![alt text](imgs/mdk5/img-9.jpg)
   
   然后添加头文件路径，将`sgl/include`添加到`Include Path`中，将`sgl`目录添加到`Include Path`中。                   
    ![alt text](imgs/mdk5/img-10.jpg)

#### 3.创建一个简单的demo

在`main.c`中添加如下代码：

```c
int main(void)
{
    ...
    uart_init();
    systick_init();
    tft_init();
    // 必须先初始化SysTick和屏幕设备，然后再初始化SGL框架
    sgl_init();
    ...

    /* 添加一个按钮 */
    sgl_obj_t *label = sgl_label_create(NULL);
    sgl_obj_set_size(label, PANEL_WIDTH, 30);
    sgl_obj_set_pos_align(label, SGL_ALIGN_CENTER);
    sgl_label_set_font(label, &consolas24);
    sgl_label_set_text(label, "Hello SGL!");

    while(1) {
        sgl_task_handler();
    }

    return 0;
}
```

然后点击编译按钮，编译成功后，烧录到开发板中即可。    
![alt text](imgs/mdk5/img-11.jpg)

```{note}
如果发现颜色显示不正确，请查看屏幕驱动芯片手册，是否存在16位颜色交换模式，如果存在，可以使用下面几种方式任意一种解决：
1. 修改`sgl_config.h`文件，将`CONFIG_SGL_COLOR16_SWAP`定义为1，使用软件交换颜色
2. 查看屏幕驱动芯片手册，设置16位颜色交换模式。
3. 配置MCU的SPI外设，以16位发送
```

### 触摸屏支持

SGL支持触摸屏，用户可以使用触摸屏来控制SGL的控件，例如点击按钮，滑动列表等等。触摸的底层对接有两种方式，一种是使用中断，一种是使用定时轮询，这里以定时轮询为例说明。
用户只需要在定时轮询函数中添加如下代码：

```c
/* 定时轮询函数，一般设置10~30ms */
void touch_timer_handle(void)
{
    bool pressed;
    int16_t x, y;

    /* 获取触摸屏的坐标和是否按下 */
    pressed = touch_get_pressed();
    x = touch_get_x();
    y = touch_get_y();

    /* 调用SGL的触摸事件处理函数 */
    sgl_event_pos_input(x, y, pressed);
}
```

### DMA双缓冲支持

SGL支持DMA双缓冲，用户可以使用DMA来提高图形刷新效率，用户需要使用双缓冲来避免屏幕闪烁，如下方式可使用双缓冲：

```c
sgl_color_t panel_buffer1[PANEL_WIDTH * 10];
sgl_color_t panel_buffer2[PANEL_WIDTH * 10];

sgl_fbinfo_t fbinfo = {
    .xres = PANEL_WIDTH,
    .yres = PANEL_HEIGHT,
    .flush_area = panel_flush_area,
    .buffer[0] = panel_buffer1,
    .buffer[1] = panel_buffer2,
    .buffer_size = SGL_ARRAY_SIZE(panel_buffer1), 
};
```

上面的代码中，panel_buffer1和panel_buffer2是双缓冲，并且panel_buffer1和panel_buffer2的buffer_size必须一致，buffer_size为缓冲区大小，这里设置为10行，即10行数据。        
并且sgl_fbdev_flush_ready()函数在DMA完成中断处理函数中调用，如下代码：

```c
void dma_complete_cb(void){
    /*清除中断判断之类需要自己实现*/
    sgl_fbdev_flush_ready();
}

void panel_flush_area(sgl_area_t *area, sgl_color_t *src){
    tft_set_win(area->x1, area->y1, area->x2, area->y2);
    GPIO_WriteBit(SPI_DC_PORT,SPI_DC_PIN,1);
    //非阻塞函数
    DMA_SendData_NoWait(src, (area->x2 - area->x1 + 1) * (area->y2 - area->y1 + 1)* sizeof(sgl_color_t));        
}
```

### LCD控制器方式

LCD支持直接向屏幕控制器显存直接写入数据，对于有LCD控制器的屏幕，可以直接向控制器的显存中写数据，这样不需要再进行DMA拷贝，从而提高效率，使用方法如下：

1. 在配置文件中添加如下配置：
   
   ```c
   #define    CONFIG_SGL_USE_FBDEV_VRAM         1
   ```
   
   这里的CONFIG_SGL_USE_FBDEV_VRAM为1表示使用LCD控制器方式      

2. 注册Framebuffer设备，代码如下：

```c
void lcd_flush(sgl_area_t *area, sgl_color_t *src)          
{
    你需要刷新LCD，这里省略代码
    // 通知SGL刷新完成
    sgl_fbdev_flush_ready();
}

sgl_fbinfo_t fbinfo = {
    .xres = PANEL_WIDTH,
    .yres = PANEL_HEIGHT,
    .flush_area = lcd_flush,
    .buffer[0] = lcd_addr, //这里指向LCD的显存地址
    .buffer_size = LCD_WIDTH * LCD_HEIGHT,
};

// 注册Framebuffer设备
sgl_fbdev_register(&fbinfo);
```
