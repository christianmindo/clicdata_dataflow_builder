"""Distinguish bracketed field references from literal JSON/text in static lint."""
from lint_flow import expression_fields

assert expression_fields("'[ 1, 2 ]'") == set()
assert expression_fields("CASE WHEN [Flag] = 1 THEN '[{\"x\":2}]' ELSE '[]' END") == {'Flag'}
assert expression_fields("'It''s [text]' + [Actual]") == {'Actual'}
assert expression_fields("[Missing] + '[Existing]' ") == {'Missing'}
print('PASS: JSON literals, escaped quotes and real missing-field references')
