from datetime import datetime, timedelta

class EventBST:
    class __node__:
        def __init__(self, date_time, duration, name, guests):
            self.date_time = date_time  # unique key
            self.duration = duration
            self.name = name
            self.guests = guests
            self.left = None
            self.right = None
            self.size = 1

    def __init__(self):
        self.root = None

    # ---------- Utility ----------
    def __get_size(self, node):
        return node.size if node else 0

    def __update_size(self, node):
        if node:
            node.size = 1 + self.__get_size(node.left) + self.__get_size(node.right)

    # ---------- Scheduling Constraints ----------
    def __can_schedule(self, node, date_time, duration):
        """Check constraints: max 2 per day, <=5 hrs, >=3 hrs apart."""
        if duration > 5:
            print("❌ Event exceeds max duration of 5 hours.")
            return False

        date = date_time.date()
        events_same_day = self.__events_on_date(self.root, date)

        if len(events_same_day) >= 2:
            print("❌ Already 2 events scheduled on this day.")
            return False

        for ev in events_same_day:
            start = ev.date_time
            end = ev.date_time + timedelta(hours=ev.duration)
            new_start = date_time
            new_end = date_time + timedelta(hours=duration)

            # Ensure at least 3 hrs gap
            if abs((new_start - end).total_seconds()) < 3*3600 and new_start >= start:
                print("❌ Minimum 3-hour gap not maintained.")
                return False
            if abs((start - new_end).total_seconds()) < 3*3600 and start >= new_start:
                print("❌ Minimum 3-hour gap not maintained.")
                return False

        return True

    def __events_on_date(self, node, date):
        if not node:
            return []
        res = []
        if node.date_time.date() == date:
            res.append(node)
        res.extend(self.__events_on_date(node.left, date))
        res.extend(self.__events_on_date(node.right, date))
        return res

    # ---------- Add Event ----------
    def add_event(self, date_time, duration, name, guests):
        if self.__can_schedule(self.root, date_time, duration):
            self.root = self.__insert(self.root, date_time, duration, name, guests)
            print(f"✅ Event '{name}' scheduled at {date_time} for {guests} guests.")
        else:
            print(f"⚠️ Could not schedule event '{name}'.")

    def __insert(self, node, date_time, duration, name, guests):
        if node is None:
            return self.__node__(date_time, duration, name, guests)
        if date_time < node.date_time:
            node.left = self.__insert(node.left, date_time, duration, name, guests)
        elif date_time > node.date_time:
            node.right = self.__insert(node.right, date_time, duration, name, guests)
        else:
            print("❌ Event already exists at this time.")
        self.__update_size(node)
        return node

    # ---------- Cancel Event ----------
    def cancel_event(self, date_time):
        self.root = self.__delete(self.root, date_time)
        print(f"🗑️ Event at {date_time} cancelled.")

    def __delete(self, node, key_time):
        if node is None:
            return None
        if key_time < node.date_time:
            node.left = self.__delete(node.left, key_time)
        elif key_time > node.date_time:
            node.right = self.__delete(node.right, key_time)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self.__find_min(node.right)
            node.date_time, node.duration, node.name, node.guests = \
                temp.date_time, temp.duration, temp.name, temp.guests
            node.right = self.__delete(node.right, temp.date_time)
        self.__update_size(node)
        return node

    def __find_min(self, node):
        while node.left:
            node = node.left
        return node

    # ---------- Display Events in Descending Order ----------
    def display_events_desc(self):
        print("\n📅 Events (latest first):")
        self.__desc(self.root)
        print()

    def __desc(self, node):
        if node:
            self.__desc(node.right)
            print(f"{node.date_time} | {node.name} | Guests: {node.guests} | Duration: {node.duration} hrs")
            self.__desc(node.left)

    # ---------- Delete Completed Events ----------
    def delete_completed_events(self, current_time):
        self.root = self.__delete_completed(self.root, current_time)

    def __delete_completed(self, node, current_time):
        if not node:
            return None
        node.left = self.__delete_completed(node.left, current_time)
        node.right = self.__delete_completed(node.right, current_time)

        if node.date_time + timedelta(hours=node.duration) < current_time:
            print(f"🗑️ Deleting completed event: {node.name} at {node.date_time}")
            return self.__delete(node, node.date_time)

        self.__update_size(node)
        return node

if __name__ == "__main__":
    bst = EventBST()

    # Schedule events
    bst.add_event(datetime(2025, 9, 15, 10), 4, "Conference", 100)
    bst.add_event(datetime(2025, 9, 15, 16), 3, "Workshop", 50)  # OK
    bst.add_event(datetime(2025, 9, 15, 20), 2, "Dinner", 30)   # ❌ exceeds 2 per day

    bst.add_event(datetime(2025, 9, 16, 11), 5, "Wedding", 200)
    bst.add_event(datetime(2025, 9, 16, 14), 3, "Reception", 150)  # ❌ less than 3 hr gap

    # Display events in descending order
    bst.display_events_desc()

    # Cancel event
    bst.cancel_event(datetime(2025, 9, 15, 16))
    bst.display_events_desc()

    # Delete completed events
    bst.delete_completed_events(datetime(2025, 9, 17, 0))
    bst.display_events_desc()
