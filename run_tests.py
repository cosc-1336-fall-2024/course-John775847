import unittest

# from tests.homework.b_in_proc_out import tests_in_proc_out

# suiteb = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
# unittest.TextTestRunner(verbosity=2).run(suiteb)

# from tests.homework.c_decisions import tests_decisions
# suitec = unittest.TestLoader().loadTestsFromModule(tests_decisions)
# unittest.TextTestRunner(verbosity=2).run(suitec)

# from tests.homework.d_repetition import tests_repetition
# suited = unittest.TestLoader().loadTestsFromModule(tests_repetition)
# unittest.TextTestRunner(verbosity=2).run(suited)

from tests.homework.e_functions import tests_functions
suitee = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suitee)
