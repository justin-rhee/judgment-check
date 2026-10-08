from pathlib import Path
import io
import unittest

path=Path(__file__).with_name('test_skills.py')
source=path.read_text()
old=" or not fields.get('description')"
assert old in source
scope={'__file__':str(path),'__name__':'mutation_fixture'}
exec(compile(source.replace(old,'',1),str(path),'exec'),scope)
suite=unittest.TestSuite([scope['SkillTests']('test_missing_description_is_rejected')])
result=unittest.TextTestRunner(stream=io.StringIO()).run(suite)
assert len(result.failures)==1 and not result.errors, 'missing-description check is not load-bearing'
print('load-bearing mutation: expected assertion failure observed')
