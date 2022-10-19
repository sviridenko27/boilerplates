import datetime

from garbage.clients.autograph.client import AutographService

service = AutographService()

schemas = service.get_schemas()
print(schemas)

schema_id = schemas[0]["ID"]
cars = service.get_schema_cars_simple(schema_id=schema_id)
print(cars)

datetime_start = datetime.datetime(year=2022, month=10, day=10, hour=00, minute=00)
datetime_end = datetime.datetime(year=2022, month=10, day=10, hour=23, minute=59)


statistics = service.get_cars_statistic(datetime_start, datetime_end, cars, schema_id)
print(statistics)






