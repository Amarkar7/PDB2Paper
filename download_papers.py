#!/usr/bin/env python3
# =========================================================


def main():

    pdb_ids = load_pdb_ids()

    print(f"Total PDB IDs : {len(pdb_ids)}")

    for pdb_id in tqdm(pdb_ids):

        print("\n" + "=" * 80)
        print(f"PROCESSING : {pdb_id}")

        output_file = os.path.join(
            OUTPUT_DIR,
            f"{pdb_id}.pdf"
        )

        if os.path.exists(output_file):

            print("[ALREADY DOWNLOADED]")

            continue

        doi, title = get_doi_from_pdb(pdb_id)

        if not doi:

            print("[NO DOI FOUND]")

            save_failed(pdb_id)

            continue

        print(f"DOI   : {doi}")
        print(f"TITLE : {title}")

        pdf_link = find_pdf_link(doi)

        if not pdf_link:

            print("[PDF LINK NOT FOUND]")

            save_failed(pdb_id)

            continue

        print("[PDF FOUND]")
        print(pdf_link)

        success = download_pdf(
            pdf_link,
            output_file
        )

        if success:

            print(f"[DOWNLOADED] {output_file}")

        else:

            print("[FAILED DOWNLOAD]")

            save_failed(pdb_id)

        sleep_time = random.uniform(3, 8)

        print(f"[SLEEPING {sleep_time:.1f} sec]")

        time.sleep(sleep_time)

    print("\nDONE")
    print(f"FAILED IDS SAVED IN : {FAILED_FILE}")


if __name__ == "__main__":
    main()
