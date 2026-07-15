## 图片取模

图片取模实际上是将图片数据转换为pixmap数据，但是针对不同的控件，其支持的pixmapdata格式不同，因此需要将图片数据转换为对应的pixmapdata数据。

### 普通控件的pixmap支持

普通控件(按钮，矩形，圆，进度条等)的pixmap仅支持相应颜色为的格式，不支持压缩，也不支持外部Flash，例如，屏幕的颜色是RGB565的，那么取模时选择的颜色格式必须为RGB565，否则会出错，如果屏幕是RGB888的，那么取模时选择的颜色格式必须为RGB888，否则会出错。

### img控件的图片支持

img控件支持RGB332, RGB565，RGB888，并且支持RLE压缩格式，同时支持外部Flash。

### img_ext控件的图片支持

img_ext控件支持img的基本功能，额外支持任意旋转、独立 X/Y 缩放，无这些需求建议使用img。      

### 取模步骤

1. 点击左侧的导航栏中的【图片取模工具】
2. 点击【📁 点击或拖拽图片到此处 支持格式：JPG、JPEG、PNG、BMP 已添加 0/1024 张图片】，选择需要转换的图片，可以多个图片一起转换
3. 选择【颜色格式】，选择你需要的颜色格式
4. 选择【输出格式】，如果是使用外部Flash，请选择bin格式，否则请选择c格式
5. 选择【压缩算法】，如果是img系列，可以支持压缩，如果是普通控件，请选择无压缩
6. 填写输出的【文件名】，默认是images文件
7. 点击【开始转换】按钮，即可生成对应的pixmap数据

### 在SGL中使用生成的pixmap数据

最终生成的数据是一个.c文件，将这个文件复制到你的工程文件中，并且添加到编译中，生成的格式如下：

```c
/* 这里省略大量数组数据 */
...
const sgl_pixmap_t pic1_pixmap = {
    .width = 131,
    .height = 128,
    .bitmap.array = pic1_data,
    .format = SGL_PIXMAP_FMT_RGB565,
};
```

在你的代码中使用如下代码：

```c
extern const sgl_pixmap_t pic1_pixmap;
sgl_xxx_set_pixmap(xxx_obj, &pic1_pixmap);
```
