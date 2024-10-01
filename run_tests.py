import unittest

# from tests.homework.b_in_proc_out import tests_in_proc_out

# suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
# unittest.TextTestRunner(verbosity=2).run(suite)

# from tests.homework.c_decisions import tests_decisions
# suite2 = unittest.TestLoader().loadTestsFromModule(tests_decisions)
# unittest.TextTestRunner(verbosity=2).run(suite2)

from tests.homework.d_repetition import tests_repetition
suite3 = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite3)
