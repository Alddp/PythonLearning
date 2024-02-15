当然，以下是一些在使用 Selenium 时常用的方法：

1. **初始化 WebDriver**：这是开始使用 Selenium 的第一步。你需要根据你的浏览器选择相应的 WebDriver。

```python
from selenium import webdriver

driver = webdriver.Chrome()  # 对于 Chrome 浏览器
driver = webdriver.Firefox()  # 对于 Firefox 浏览器
```

2. **访问页面**：使用 `driver.get()` 方法访问一个页面。

```python
driver.get("http://www.google.com")
```

3. **查找元素**：Selenium 提供了多种查找元素的方法，如通过 id、name、class name、tag name 等。

```python
element = driver.find_element_by_name('q')  # 查找 name 为 'q' 的元素
element = driver.find_element_by_id('id')  # 查找 id 为 'id' 的元素
elements = driver.find_elements_by_class_name('class')  # 查找 class 为 'class' 的所有元素
element = driver.find_element_by_tag_name('div')  # 查找 tag 为 'div' 的元素
```

4. **操作元素**：找到元素后，你可以对它进行各种操作，如输入文本、点击等。

```python
element.send_keys("some text")  # 输入文本
element.clear()  # 清除文本
element.click()  # 点击元素
```

5. **获取元素信息**：你可以获取元素的各种信息，如文本、属性值等。

```python
text = element.text  # 获取元素的文本
attr = element.get_attribute('attr')  # 获取元素的属性值
```

6. **导航**：Selenium 提供了一些方法来模拟浏览器的前进、后退和刷新操作。

```python
driver.back()  # 后退
driver.forward()  # 前进
driver.refresh()  # 刷新页面
```

7. **等待**：在自动化测试中，等待是一个重要的概念。Selenium 提供了隐式等待和显式等待两种方式。

```python
driver.implicitly_wait(10)  # 隐式等待，等待 10 秒

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myId"))  # 显式等待，等待 id 为 'myId' 的元素出现
)
```

8. **关闭浏览器**：完成测试后，你应该关闭浏览器。`driver.close()` 关闭当前窗口，而 `driver.quit()` 关闭所有窗口并退出浏览器。

```python
driver.close()  # 关闭当前窗口
driver.quit()  # 关闭所有窗口并退出浏览器
```

以上就是一些常用的 Selenium 方法。要记住，Selenium 的功能远不止这些，上面的只是一些基本的和常用的操作。你可以在 Selenium 的官方文档中找到更多的信息和示例。