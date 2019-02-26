from app import TodoItem

cleanroom = TodoItem(title="Clean my room", description="Just do it already",
                     complete=0, users_pk=1)

cleanroom.save()

cleanroom.complete = 1

items = TodoItem.all_for_users_pk(1)
print(items)
"""
cleanroom.save()


assert len(items) > 0, "find user's todo items works"
"""
