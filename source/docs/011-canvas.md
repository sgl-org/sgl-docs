## canvas控件

canvas控件实现定制化的界面，例如用户可能需要实现一个音乐频谱，

```c
void painter_func(sgl_surf_t *surf, sgl_area_t *area, sgl_obj_t *obj)
{
    for (int i = obj->coords.y1; i < obj->coords.y2; i += 10) {
        sgl_draw_fill_hline(surf, area, i, obj->coords.x1, obj->coords.x2, 5, SGL_COLOR_BLACK, 255);
    }
}

sgl_obj_t *canvas = sgl_canvas_create(NULL);
sgl_obj_set_pos(canvas, 10, 10);
sgl_obj_set_size(canvas, 200, 100);
sgl_canvas_set_painter_cb(canvas, painter_func);
```

上面的代码中，使用sgl_canvas_set_painter_cb()函数设置绘制函数，绘制函数的参数说明如下：   

- 1. surf: 绘制的缓冲区
- 2. area: 绘制的区域
- 3. obj: 绘制的控件对象      

其中surf和area参数在使用底层绘图函数时会使用到，底层绘图函数都在sgl_draw.h中定义，你可以参考该文件，obj参数是绘制的控件对象，你可以使用obj->coords.x1, obj->coords.y1, obj->coords.x2, obj->coords.y2来获取绘制的区域，你可以在该区域进行绘制。     
上面的painter_func函数使用sgl_draw_fill_hline()函数绘制水平线，每次间隔10个像素，颜色为黑色，透明度为255。

### 区域更新

当绘制的部分区域改变时，需要调用sgl_obj_update_area()函数来更新区域，如何需要更新整个控件，请使用sgl_obj_set_dirty()函数来更新整个控件区域。
