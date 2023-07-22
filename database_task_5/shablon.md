```sql
class Universal:
    def __init__(self, table_name_update):
        self.table_name_update = table_name_update

    def trigger_fun(self):
        cur = connection.cursor()
        func_trigger = f"""create or replace function {self.table_name_update}_data_update_trigger_func()
                returns trigger
                language plpgsql
                        as
                        $$
                        BEGIN
                        if tg_op = 'UPDATE' THEN
                            insert into logs(detail, old_data, new_data, table_name)
                            values ('Updated.', row_to_json(OLD), row_to_json(NEW), {self.table_name_update});
                            return NEW;
                        elsif tg_op = 'DELETE' THEN
                            insert into logs(detail, old_data, table_name)
                            values ('DELETED.', row_to_json(OLD), {self.table_name_update});
                            return OLD;
                        END IF;
                        end;
                        $$;"""
        cur.execute(func_trigger)
        connection.commit()

    def trigger(self):
        trigger = f"""
        create trigger {self.table_name_update}_data_update_trigger
        after update or delete
        on {self.table_name_update}
        for each row
    execute procedure {self.trigger_fun()};
        """
        cur.execute(trigger)
        connection.commit()

```