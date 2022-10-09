import sys
import csvCalorieCounter

if len(sys.argv) > 1:
    cmd = sys.argv[1]
    if cmd == 'list':
        if len(sys.argv) > 3 and sys.argv[2] == 'eaten':
            csvCalorieCounter.list_eaten(sys.argv[3], sys.argv[4])
        else:
            if sys.argv[2] == 'weights' and len(sys.argv) > 3:
                csvCalorieCounter.list_weights(sys.argv[3])
            elif sys.argv[2] == 'dates' and len(sys.argv) > 3:
                csvCalorieCounter.list_dates(sys.argv[3])
            elif sys.argv[2] == 'foods':
                csvCalorieCounter.list_foods()
    elif cmd == 'lookup':
        if len(sys.argv) > 2:
            if sys.argv[2] == 'calories':
                csvCalorieCounter.lookup_calories(sys.argv[3])
            elif sys.argv[2] == 'weight' and len(sys.argv) > 3:
                csvCalorieCounter.lookup_weight(sys.argv[3], sys.argv[4])
    elif cmd == 'total':
        if len(sys.argv) > 2:
            csvCalorieCounter.total_date(sys.argv[2], sys.argv[3])
    elif cmd == 'newuser':
        if len(sys.argv) > 2:
            csvCalorieCounter.new_user(sys.argv[2])
    elif cmd == 'eaten':
        if len(sys.argv) > 4:
            csvCalorieCounter.eaten(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == 'weighed':
        if len(sys.argv) > 3:
            csvCalorieCounter.weighed(sys.argv[2], sys.argv[3])
    else:
        print('Invalid option selected. Please try another input!')

