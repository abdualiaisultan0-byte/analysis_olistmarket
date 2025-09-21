import os
from pathlib import Path
import csv
import psycopg2

try:
    from dotenv import load_dotenv  
    load_dotenv()
except Exception:
    pass

DB = dict(
    host="localhost",
    port=5432,
    dbname="project_olist",
    user="postgres",
    password="Aisultan_06",
)

QUERIES_FILE = Path("queries.sql")
OUT_DIR = Path("outputs")
SAVE_TO_CSV = True  


def split_sql_with_labels(text: str):
    """
    Делит файл по ';' и присваивает метку из комментария вида '-- Q6: ...'.
    Возвращает список (label, sql).
    """
    blocks, buf, label = [], [], "QUERY"
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("-- Q"):
            
            try:
                label = s.split()[1].rstrip(":")  
            except Exception:
                label = "QUERY"
        buf.append(line)
        if s.endswith(";"):
            sql = "\n".join(buf).strip()
            if any(not ln.strip().startswith("--") and ln.strip() for ln in buf):
                blocks.append((label, sql))
            buf, label = [], "QUERY"
    return blocks


def print_tables():
    with psycopg2.connect(**DB) as conn, conn.cursor() as cur:
        cur.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
            ORDER BY table_name;
            """
        )
        print("Таблицы в project_olist:")
        for (t,) in cur.fetchall():
            print(" -", t)


def run_queries():
    if not QUERIES_FILE.exists():
        print(f"[!] Не найден {QUERIES_FILE.resolve()}")
        return

    OUT_DIR.mkdir(exist_ok=True)
    text = QUERIES_FILE.read_text(encoding="utf-8")
    queries = split_sql_with_labels(text)

    if not queries:
        print("[!] В queries.sql не найдено запросов (убедись, что каждый заканчивается на ';').")
        return

    with psycopg2.connect(**DB) as conn, conn.cursor() as cur:
        for label, sql in queries:
            print(f"\n=== {label} ===")
            try:
                cur.execute(sql)

                if cur.description:
                    cols = [d[0] for d in cur.description]
                    rows = cur.fetchall()

                    print(f"{len(rows)} rows")
                    preview = rows[:5]
                    for r in preview:
                        print(dict(zip(cols, r)))

                    if SAVE_TO_CSV:
                        out_path = OUT_DIR / f"{label}.csv"
                        with out_path.open("w", newline="", encoding="utf-8") as f:
                            w = csv.writer(f)
                            w.writerow(cols)
                            w.writerows(rows)
                else:
                    print(f"Done. {cur.rowcount} rows affected.")

            except Exception as e:
                print(f"ERROR in {label}: {e}")


def main():
    print_tables()
    run_queries()


if __name__ == "__main__":
    main()
