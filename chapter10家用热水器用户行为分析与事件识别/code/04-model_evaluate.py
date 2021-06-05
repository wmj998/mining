# 代码10-9

# 模型评价
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
import joblib
import matplotlib.pyplot as plt

bpnn = joblib.load('../tmp/water_heater_nnet.m')  # 加载模型
y_pred = bpnn.predict(x_stdtest)  # 返回预测结果
print('神经网络预测结果评价报告：\n', classification_report(y_test, y_pred))
# 绘制roc曲线图
plt.rcParams['font.sans-serif'] = 'SimHei'  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
fpr, tpr, thresholds = roc_curve(y_pred, y_test)  # 求出TPR和FPR
plt.figure(figsize=(6, 4))  # 创建画布
plt.plot(fpr, tpr)  # 绘制曲线
plt.title('用户用水事件识别ROC曲线')  # 标题
plt.xlabel('FPR')  # x轴标签
plt.ylabel('TPR')  # y轴标签
plt.savefig('../tmp/用户用水事件识别ROC曲线.png')  # 保存图片
plt.show()  # 显示图形
