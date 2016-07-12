from validation.pipeline.validation_task import InputIteratorTask
import config as vnet_config


class vnetInputIterator(InputIteratorTask):
	def run(self):
		print "Welcome to the VNET pipeline validation"

		fold_index = 1
		for fold in miccai_config.dataset:
			for input in fold:
				yield [fold_index, input]
			fold_index += 1

	def __len__(self):
		fold_lens = map(lambda fold: len(fold), miccai_config.dataset)
		return reduce(lambda a,b: a+b, fold_lens)