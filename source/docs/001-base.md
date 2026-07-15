## SGL基础知识

### page概念

SGL中的page表示一个绘制页面，其大小为屏幕的宽和高，无法改变，所有的控件都绘制在page中，也就是page是所有的控件的根控件。在调用sgl_init()时就默认创建一个page，作为一个活动的page。
用户也可以自己创建一个page，用来做多页面切换显示。

#### 页面创建（根控件创建）

使用sgl_obj_create(NULL)函数创建一个pag，函数原型如下：

```c
sgl_obj_t* sgl_obj_create(sgl_obj_t *parent);
```

例如下面创建两个页面，然后将第二个页面作为活动页面：

```c
sgl_obj_t *page1 = sgl_obj_create(NULL);
sgl_obj_t *page2 = sgl_obj_create(NULL);
sgl_screen_load(page2);
```

#### 设置背景色

使用sgl_page_set_color()函数设置页面的背景色，函数原型如下：

```c
void sgl_page_set_color(sgl_obj_t* obj, sgl_color_t color);
```

#### 设置页面背景图片

使用sgl_page_set_pixmap()函数设置页面的背景图片，函数原型如下：
sds

```c
void sgl_page_set_pixmap(sgl_obj_t* obj, const sgl_pixmap_t *pixmap);
```

例如下面创建一个页面，并设置其背景图片为test_pixmap：

```c
extern const unsigned char gImage_test[7080];
const sgl_pixmap_t test_pixmap = {
    .width = 60,
    .height = 59,
    .bitmap = gImage_test,
};

sgl_obj_t *page = sgl_obj_create(NULL);
sgl_page_set_pixmap(page, &test_pixmap);
```

### 控件删除

在一些情况下，用户需要删除一个控件，可以使用sgl_obj_delete()函数，函数原型如下：

```c
void sgl_obj_delete(sgl_obj_t *obj);
```

例如下面创建一个按钮，并删除该按钮：

```c
sgl_obj_t *btn = sgl_button_create(NULL);
sgl_obj_set_pos(btn, 10, 10);
sgl_obj_set_size(btn, 100, 50);
.....
sgl_obj_delete(btn);
```

```{tip}
删除控件时，如果该控件有子控件，则子控件也会被删除。如果使用sgl_obj_delete(NULL)，则会删除当前活动页面的所有控件，但不会删除该页面。如果使用gl_obj_delete(page1)，则会删除page1，并且page1的所有子控件也被删除。
```

### 控件层级设置

SGL的所有控件不仅仅有父子关系，还有层级关系，即控件的绘制顺序，对于兄弟控件，即父控件下的多个控件，绘制顺序是先绘制先创建的控件，再绘制后创建的控件，从视觉上来说，如果存在重叠，则后创建的控件会覆盖先创建的控件。
用户可以使用sgl_obj_move_up, sgl_obj_move_down, sgl_obj_move_top, sgl_obj_move_bottom函数来设置控件的层级关系，函数原型如下：

```c
void sgl_obj_move_up(sgl_obj_t *obj);
void sgl_obj_move_down(sgl_obj_t *obj);
void sgl_obj_move_top(sgl_obj_t *obj);
void sgl_obj_move_bottom(sgl_obj_t *obj);
```

- sgl_obj_move_up函数用于将控件上移一个层级
- sgl_obj_move_down函数用于将控件下移一个层级
- sgl_obj_move_top函数用于将控件移到最上层
- sgl_obj_move_bottom函数用于将控件移到最下层

```{note}
上面的函数只能对控件的层级关系有效，不会改变控件的父子关系。如果控件A和控件B的父控件是同一个，则上面的函数是有效的，否则无效。
```

### 立刻更新屏幕

SGL的屏幕刷新机制是异步的，当用户创建一个控件时，该控件仅仅是添加到了SGL的系统控件树中，并不会立刻刷新，必须等SGL系统滴答时钟触发时，才会刷新屏幕。如果用户此时需要立刻更新屏幕，可以使用sgl_task_handler_sync函数，函数原型如下：

```c
void sgl_task_handler_sync(void);
```

该函数会立刻绘制一次SGL的系统控件树中的所有控件，并刷新到屏幕上。

### 控件隐藏和显示

使用sgl_obj_set_hidden函数可以隐藏一个控件，函数原型如下：

```c
void sgl_obj_set_hidden(sgl_obj_t *obj);
```

使用sgl_obj_set_visible函数可以显示一个控件，函数原型如下：

```c
void sgl_obj_set_visible(sgl_obj_t *obj);
```

### 设置控件事件回调函数

使用sgl_obj_set_event_cb函数设置控件的事件回调函数，函数原型如下：

```c
void sgl_obj_set_event_cb(sgl_obj_t *obj, void (*event_fn)(sgl_event_t *e), size_t data)
```

该函数用于设置控件的事件回调函数，当用户点击控件时，SGL会调用该回调函数，并传入一个sgl_event_t结构体指针，该结构体中包含了点击事件的信息。
例如下面：

```c
...
void button_event_cb(sgl_event_t *evt)
{
    size_t para = evt->param;
    switch (evt->type) {
    case SGL_EVENT_PRESSED:
        printf("Button %d pressed\n", para);
        break;
    case SGL_EVENT_RELEASED:
        printf("Button %d released\n", para);
        break; 
    }
}
...
sgl_obj_t *button = sgl_button_create(NULL);
sgl_obj_set_pos(button, 20, 20);
sgl_obj_set_size(button, 200, 100);
sgl_obj_set_event_cb(button, button_event_cb, xxx_ptr);
...
```
