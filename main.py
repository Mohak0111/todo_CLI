from store import Store
from menus import main_menu, list_task
from input_validator import choice_validator, string_validator, int_validator, id_retry

def main():
    store=Store()
    while True: # main menu
        main_choice=choice_validator(*main_menu)
        if main_choice==1:
            while True: # list task menu
                list_choice=choice_validator(*list_task)
                if list_choice==1:
                    # display all tasks
                    ans=store.get_all()
                    if not len(ans):
                        print("No tasks to display.")
                    else:
                        print(ans)
                if list_choice==2:
                    # display pending tasks
                    ans=store.get_pending()
                    if not len(ans):
                        print("No tasks pending.")
                    else:
                        print(ans)
                if list_choice==3:
                    # display complete tasks
                    ans=store.get_complete()
                    if not len(ans):
                        print("No tasks completed.")
                    else:
                        print(ans)
                if list_choice==4:
                    break
        if main_choice==2:
            task_str=string_validator("\nEnter task: ")
            store.add_task(task_str)
        if main_choice==3:
            while True:
                task_id=int_validator("\nEnter task ID to be deleted: ")
                id_status=store.id_status(task_id)
                if id_status=="-1":
                    print("ERROR: Task ID not found.")
                    retry_choice=id_retry("Try another ID?(y/n)")
                    if retry_choice==0:
                        break
                else:
                    store.delete_task(task_id)
                    print("Task deleted successfully")
                    break
        if main_choice==4: # complete task
            while True:
                task_id=int_validator("\nEnter task ID to be completed: ")
                id_status=store.id_status(task_id)
                if id_status=="-1":
                    print("ERROR: Task ID not found.")
                    retry_choice=id_retry("Try another ID?(y/n)")
                    if retry_choice==0:
                        break
                elif id_status=="complete":
                    print("ERROR: Task already complete.")
                    retry_choice=id_retry("Try another ID?(y/n)")
                    if retry_choice==0:
                        break
                    break
                else:
                    store.complete_task(task_id)
                    print("Task completed successfully")
                    break
        if main_choice==5:
            print("\nExiting...\n")
            store.write_state()
            break

if __name__=="__main__":
    main()