try:
    import unittest2 as unittest
except:
    import unittest

from Orange.testing import testing
from Orange.testing.testing import datasets_driven, test_on_datasets

@datasets_driven(datasets=testing.CLASSIFICATION_DATASETS)
class TestBoosting(testing.LearnerTestCase):
    def setUp(self):
        import orngEnsemble, orngTree
        self.learner = orngEnsemble.BoostedLearner(orngTree.TreeLearner)

    @test_on_datasets(datasets=["iris"])
    def test_pickling_on(self, dataset):
        testing.LearnerTestCase.test_pickling_on(self, dataset)

@datasets_driven(datasets=testing.CLASSIFICATION_DATASETS + \
                 testing.REGRESSION_DATASETS)
class TestBagging(testing.LearnerTestCase):
    def setUp(self):
        import orngEnsemble, orngTree
        self.learner = orngEnsemble.BaggedLearner(orngTree.TreeLearner)

    @test_on_datasets(datasets=["iris"])
    def test_pickling_on(self, dataset):
        testing.LearnerTestCase.test_pickling_on(self, dataset)


@datasets_driven(datasets=testing.CLASSIFICATION_DATASETS)
class TestRandomForest(testing.LearnerTestCase):
    def setUp(self):
        import orngEnsemble, orngTree
        self.learner = orngEnsemble.RandomForestLearner()

    @test_on_datasets(datasets=testing.CLASSIFICATION_DATASETS + \
                      testing.REGRESSION_DATASETS)
    def test_pickling_on(self, dataset):
        testing.LearnerTestCase.test_pickling_on(self, dataset)


@datasets_driven(datasets=testing.CLASSIFICATION_DATASETS)
class TestStacking(testing.LearnerTestCase):
    def setUp(self):
        from Orange.ensemble import stacking
        from Orange.classification import tree, bayes
        self.learner = stacking.StackedClassificationLearner(
            [tree.TreeLearner(), bayes.NaiveLearner()], folds=5
        )

    @test_on_datasets(datasets=["iris"])
    def test_pickling_on(self, dataset):
        testing.LearnerTestCase.test_pickling_on(self, dataset)


if __name__ == "__main__":
    import unittest
    unittest.main()
