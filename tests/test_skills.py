from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
NAMES=('judgment-loop','scale-the-lesson','seat-model-migration')


def validate(path):
    text=path.read_text()
    parts=text.split('---',2)
    if len(parts)!=3 or parts[0].strip():
        raise ValueError('missing frontmatter')
    fields={}
    for line in parts[1].strip().splitlines():
        key,sep,value=line.partition(':')
        if not sep or not value.strip(): raise ValueError('invalid frontmatter field')
        fields[key.strip()]=value.strip()
    if fields.get('name')!=path.parent.name or not fields.get('description'):
        raise ValueError('missing or mismatched discovery metadata')
    if not parts[2].strip(): raise ValueError('empty instructions')
    for target in re.findall(r'\]\(([^)]+)\)',parts[2]):
        if '://' in target or target.startswith('#'): continue
        resolved=(path.parent/target.split('#')[0]).resolve()
        if path.parent.resolve() not in resolved.parents or not resolved.is_file():
            raise ValueError('unbundled reference')
    return fields


class SkillTests(unittest.TestCase):
    def test_all_three_skills_load(self):
        for name in NAMES:
            self.assertEqual(validate(ROOT/'skills'/name/'SKILL.md')['name'],name)

    def test_bundle_contains_only_selected_skill_files(self):
        files={str(p.relative_to(ROOT/'skills')) for p in (ROOT/'skills').rglob('*') if p.is_file()}
        self.assertEqual(files,{name+'/SKILL.md' for name in NAMES})
        self.assertFalse(any(p.is_symlink() for p in (ROOT/'skills').rglob('*')))

    def test_documented_copy_installs_without_source_tree(self):
        with tempfile.TemporaryDirectory() as d:
            dest=Path(d)/'.agents/skills';dest.mkdir(parents=True)
            for name in NAMES:
                shutil.copytree(ROOT/'skills'/name,dest/name)
            for name in NAMES:
                validate(dest/name/'SKILL.md')
                self.assertEqual((dest/name/'SKILL.md').read_bytes(),(ROOT/'skills'/name/'SKILL.md').read_bytes())

    def test_missing_description_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'fixture';p.mkdir();file=p/'SKILL.md'
            file.write_text('---\nname: fixture\n---\n# Instructions\n')
            with self.assertRaisesRegex(ValueError,'metadata'):validate(file)

    def test_unbundled_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'fixture';p.mkdir();file=p/'SKILL.md'
            file.write_text('---\nname: fixture\ndescription: fixture\n---\n[Read](missing.md)\n')
            with self.assertRaisesRegex(ValueError,'unbundled'):validate(file)

    def test_external_file_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'fixture';p.mkdir();(Path(d)/'outside.md').write_text('external')
            file=p/'SKILL.md';file.write_text('---\nname: fixture\ndescription: fixture\n---\n[Read](../outside.md)\n')
            with self.assertRaisesRegex(ValueError,'unbundled'):validate(file)


if __name__=='__main__':unittest.main(verbosity=2)
