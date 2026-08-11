from pathlib import Path


LOG_DIR = Path("/var/www/code/exceptions")


logs = {
    "exception_001.log": """\
2026-08-11 10:31:42 ERROR
request_id=req-9f821
user_id=USR-10001
service=checkout-service
endpoint=/api/checkout
exception=PaymentGatewayTimeout
message=Payment gateway did not respond within 30 seconds
stack_trace=PaymentGatewayClient.charge -> HTTP timeout
severity=HIGH
""",

    "exception_002.log": """\
2026-08-11 10:34:17 ERROR
request_id=req-a8219
user_id=USR-10003
service=checkout-service
endpoint=/api/checkout
exception=InventoryServiceTimeout
message=Inventory service connection timed out
stack_trace=InventoryClient.reserve -> ConnectionTimeout
severity=HIGH
""",

    "exception_003.log": """\
2026-08-11 10:37:51 ERROR
request_id=req-b7214
user_id=USR-10002
service=payment-service
endpoint=/api/payment
exception=PaymentDeclined
message=Payment provider declined the transaction
stack_trace=PaymentService.process -> ProviderDeclined
severity=MEDIUM
""",

    "exception_004.log": """\
2026-08-11 10:42:08 ERROR
request_id=req-c8921
user_id=USR-10001
service=order-service
endpoint=/api/orders
exception=DatabaseDeadlock
message=Transaction rolled back because of database deadlock
stack_trace=OrderRepository.create -> DeadlockFound
severity=HIGH
""",

    "exception_005.log": """\
2026-08-11 10:45:33 ERROR
request_id=req-d9912
user_id=USR-10005
service=cart-service
endpoint=/api/cart
exception=RedisConnectionError
message=Unable to connect to Redis cache
stack_trace=CartService.getCart -> RedisConnectionError
severity=MEDIUM
""",

    "exception_006.log": """\
2026-08-11 10:51:12 ERROR
request_id=req-e7211
service=notification-service
endpoint=/internal/notifications
exception=SMTPConnectionError
message=Unable to connect to SMTP server
stack_trace=NotificationService.send -> SMTPConnectionError
severity=LOW
""",

    "exception_007.log": """\
2026-08-11 10:55:47 ERROR
request_id=req-f8821
user_id=USR-10007
service=checkout-service
endpoint=/api/checkout
exception=PaymentGatewayTimeout
message=Payment gateway did not respond within 30 seconds
stack_trace=PaymentGatewayClient.charge -> HTTP timeout
severity=HIGH
""",

    "exception_008.log": """\
2026-08-11 11:02:19 ERROR
request_id=req-g1822
user_id=USR-10008
service=order-service
endpoint=/api/orders
exception=OrderCreationFailed
message=Unable to create order after successful payment
stack_trace=OrderService.create -> TransactionError
severity=HIGH
""",
}


def create_logs():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    for filename, content in logs.items():
        path = LOG_DIR / filename
        path.write_text(content)

    print(f"Created {len(logs)} exception logs in {LOG_DIR}")


if __name__ == "__main__":
    create_logs()