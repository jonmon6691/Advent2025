# Go ahead. Make my day.

import os
import sys
import shutil
import pathlib


def fatal(msg: str, code: int = 1) -> None:
	print(f"Error: {msg}", file=sys.stderr)
	sys.exit(code)


def make_day(dest_day: int, template_dir: str = "DayN") -> None:
	src = pathlib.Path(template_dir)
	if not src.exists() or not src.is_dir():
		fatal(f"template directory '{template_dir}' not found")

	day_str = str(dest_day)
	day_padded = f"{dest_day:02d}"
	dest = pathlib.Path(f"Day{day_str}")
	if dest.exists():
		fatal(f"destination directory '{dest}' already exists")

	for root, dirs, files in os.walk(src):
		root_path = pathlib.Path(root)
		rel = root_path.relative_to(src)
		# create destination directory path, with replacements
		rel_parts = [] if str(rel) == "." else rel.parts
		new_rel_parts = []
		for part in rel_parts:
			new_part = part.replace("NN", day_padded).replace("N", day_str)
			new_rel_parts.append(new_part)

		target_dir = dest.joinpath(*new_rel_parts) if new_rel_parts else dest
		target_dir.mkdir(parents=True, exist_ok=True)

		for fname in files:
			src_file = root_path / fname
			new_fname = fname.replace("NN", day_padded).replace("N", day_str)
			target_file = target_dir / new_fname

			# Try reading and templating as text; fall back to binary copy
			try:
				text = src_file.read_text(encoding="utf-8")
			except Exception:
				# binary or unreadable as text -> copy raw
				shutil.copy2(src_file, target_file)
			else:
				new_text = text.replace("NN", day_padded).replace("N", day_str)
				target_file.write_text(new_text, encoding="utf-8")
				# preserve mode
				try:
					st = src_file.stat()
					target_file.chmod(st.st_mode & 0o777)
				except Exception:
					pass


def main(argv: list[str]) -> None:
	if len(argv) < 2:
		print("Usage: mkday.py D [TEMPLATE_DIR]")
		print("Creates DayD from TEMPLATE_DIR (defaults to 'DayN')")
		sys.exit(2)

	try:
		d = int(argv[1])
	except Exception:
		fatal("first argument must be an integer day number")

	if d < 1 or d > 12:
		fatal("day number must be between 1 and 12")

	tpl = argv[2] if len(argv) >= 3 else "DayN"
	make_day(d, tpl)


if __name__ == "__main__":
	main(sys.argv)

