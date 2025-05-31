
# SniperGPT 10X USTOZ+

## Инструкция по установке и запуску:

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Запустите файл:
```
python main_ready.py
```

3. В TradingView установите Webhook и в сообщении обязательно укажите:
```
{
  "message": "BTCUSD SELL @ 104000"
}
```

Формат должен содержать поле "message", иначе сигнал не обработается.
