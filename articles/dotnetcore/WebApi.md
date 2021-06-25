# Web API

## 1 将Json字符串以Json格式返回

```C#
[HttpPost]
[Route("payment")]
public async Task<IActionResult> PostPayment()
{
    string result = await PostAsync("http://host/payment");
    return new ContentResult
    {
        ContentType = "application/json",
        Content = result
    };
}
```

## 2 