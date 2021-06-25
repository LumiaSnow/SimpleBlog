# RabbitMQ

## 开启日志工具

```bash
rabbitmq-plugins enable rabbitmq_tracing
```

## 添加Tracing日志

```bash
Pattern: #, publish.#, deliver.# #.amq.direct, #.myqueue

```

