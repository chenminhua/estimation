# 三部曲计划之「估计」

有测量就有估计，有计算就有近似，有统计就有预测

### 离散贝叶斯滤波器

this filter is a form of the g-h filter
我们用错误的百分率，来隐式计算 g 和 h。（也就是测量的不可信度）。

滤波过程为，先预测，再加入测量。 **We maka a prediction, then we correct it.**

```
prior 基于当前信念，以及系统的 behavior，预测下一时刻的状态

posterior = prior + likelihood （其中 likelihood 为测量带来的信息）
```

当我们做卡尔曼滤波的时候，其实方法是一样的，区别只是计算不同。

### 调整传感器的准确度

Another thing to note is how accurate our estimate becomes when we are in front of a door, and how it degrades when in the middle of the hallway. This should make intuitive sense. There are only a few doorways, so when the sensor tells us we are in front of a door this boosts our certainty in our position. A long stretch of no doors reduces our certainty.

## The Effect of Bad Sensor Data

One bad measurement has significantly eroded our knowledge. Now let's continue with a series of correct measurements. We quickly filtered out the bad sensor reading and converged on the most likely positions for our dog.

## Drawbacks and Limitations

Do not be mislead by the simplicity of the examples I chose. This is a robust and complete filter, and you may use the code in real world solutions. If you need a multimodal, discrete filter, this filter works.

## 局限与缺陷

第一个问题是，这里只有一个变量。
第二个问题是，这个滤波器是离散的。
第三个问题是，这玩意儿是 multimodal 的，（同时给你几个可能的答案，想象一下你的 gps 告诉你，你可能在静安区，也可能在浦东）
第四个问题是，他需要 a measurement of the change in state。就是说这个机器人要有一个运动传感器告诉它它在怎么动。

这个滤波器的优点就是：简单。

## don't lose any information
