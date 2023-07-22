import psycopg2

connection = psycopg2.connect(
    database="demo",
    user='postgres',
    password='12345',
    host='localhost',
    port=5432
)

cur = connection.cursor()


# class Universal:
#     def __init__(self, table_name_update):
#         self.table_name_update = table_name_update
#
#     def __str__(self):
#         return self.table_name_update
#
#     def func_name(self):
#         return f"{self.table_name_update}_data_update_trigger_func()"
#
#     def trigger_fun(self):
#         cur = connection.cursor()
#         func_trigger = f"""create or replace function {self.func_name()}
#                 returns trigger
#                 language plpgsql
#                         as
#                         $$
#                         BEGIN
#                         if tg_op = 'UPDATE' THEN
#                             insert into logs(detail, old_data, new_data,  select_table)
#                             values ('Updated.', row_to_json(OLD), row_to_json(NEW),{self.table_name_update});
#                             return NEW;
#                         elsif tg_op = 'DELETE' THEN
#                             insert into logs(detail, old_data,select_table)
#                             values ('DELETED.', row_to_json(OLD), {self.table_name_update});
#                             return OLD;
#                         END IF;
#                         end;
#                         $$;"""
#         cur.execute(func_trigger)
#         connection.commit()
#
#     def trigger(self,):
#         tig = connection.cursor()
#         triggers = f"""
#            create or replace trigger {self.table_name_update}_data_update_trigger
#            after update or delete
#            on {self.table_name_update}
#            for each row
#        execute procedure  {Universal(self.table_name_update).func_name()};
#
#            """
#         tig.execute(triggers)
#         connection.commit()
#
#
# a1 = Universal('seats').func_name()
# print(a1)

# def unniversal_fun(table_name_update):
#     cur = connection.cursor()
#     func_name = f"{table_name_update}_data_update_trigger_func()"
#     func_trigger = f"""create or replace function {func_name}
#             returns trigger
#             language plpgsql
#                     as
#                     $$
#                     BEGIN
#                     if tg_op = 'UPDATE' THEN
#                         insert into logs(detail, old_data, new_data, select_table)
#                         values ('Updated.', row_to_json(OLD), row_to_json(NEW), {table_name_update});
#                         return NEW;
#                     elsif tg_op = 'DELETE' THEN
#                         insert into logs(detail, old_data, select_table)
#                         values ('DELETED.', row_to_json(OLD), {table_name_update});
#                         return OLD;
#                     END IF;
#                     end;
#                     $$;"""
#     cur.execute(func_trigger)
#     connection.commit()
#     trigger = f"""
#     create trigger {table_name_update}_data_update_trigger
#     after update or delete
#     on {table_name_update}
#     for each row
# execute procedure {func_name};
#     """
#     cur.execute(trigger)
#     connection.commit()
# unniversal_fun('seats')


