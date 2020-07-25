
# Scirpt to convert pg_dump file to sqlitedb file
# Note: WIP

from config import PG_DUMP_FILE, SQLITE_DB_FILE


SW_SET = 'SET'
SW_SELECT_PG = 'SELECT pg_catalog'
SW_COMMENT = 'COMMENT ON'
SW_CREATE_EXT = 'CREATE EXTENSION'
SW_CREATE_SEQ = 'CREATE SEQUENCE'
SW_ALTER = 'ALTER'


def process(input_file=PG_DUMP_FILE, output_file=SQLITE_DB_FILE):
    """
    function to convert pg_dump file to sqlitedb file - minimalist
    """
    is_sequence = False
    is_alter = False
    pg_file = open(input_file, 'r')
    out_file = open(output_file, 'w')

    out_file.write('BEGIN;\n')

    for line_no, line in enumerate(pg_file.readlines()):
        if line.startswith(SW_CREATE_EXT):
            continue
        if line.startswith(SW_SET):
            pass
        elif line.startswith(SW_SELECT_PG):
            pass
        elif line.startswith(SW_COMMENT):
            pass
        elif line.startswith(SW_CREATE_SEQ):
            is_sequence = True
            if line.endswith(';'):
                is_sequence = False
        elif line.startswith(SW_ALTER):
            is_alter = True
            if line.endswith(';'):
                is_alter = False
        elif is_sequence or is_alter:
            if line.endswith(';'):
                # print('here')
                is_sequence = False
                is_alter = False
        elif not line.startswith('--'):
            # CREATE & INSERT STMTS
            # print(line_no, line)
            line.replace('\"public\".', '')  # Use re
            out_file.write(line)

    out_file.write('END;\n')
    out_file.close()
    pg_file.close()


process()
