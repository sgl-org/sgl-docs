## unzip_img控件

创建一个unzip_img控件，使用如下代码：

```c
sgl_obj_t *img = sgl_unzip_img_create(NULL);
sgl_obj_set_pos(img, 250, 100);
sgl_obj_set_size(img, 100, 100);
```

上面代码在默认的活动页面上创建了一个大小为100x100的unzip_img控件，并设置其位置为250,100。

### 设置透明度

使用`sgl_unzip_image_set_alpha()`函数设置图片的透明度，如下：

```c
void sgl_unzip_img_set_alpha(sgl_obj_t *obj, uint8_t alpha);

sgl_unzip_img_set_alpha(img, 128);
```

### 设置对齐方式

使用`sgl_unzip_image_set_align()`函数设置图片窗口的对齐方式，如下：

```c
void sgl_unzip_img_set_align(sgl_obj_t *obj, sgl_align_type_t align);

sgl_unzip_img_set_align(img, SGL_ALIGN_CENTER);
```

其中，`sgl_align_type_t`是SGL_ALIGN开头的宏的任一选项。
