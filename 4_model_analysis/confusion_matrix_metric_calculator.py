import csv
from collections import defaultdict

# Input and output CSV filenames
baseDir = '/Users/markfisher/Desktop/cr_moth_classification/ready_for_classification_model/'
shouldUseOptionalList = True
optionalList = ["Glena_mopsaria,I_PBA31015.jpg",
"Cliniodes_opalalis,I_MFS3188.jpg",
"Euglyphis_libnites,I_MFS10866.jpg",
"Lomographa_argentata,I_PBA19442.jpg",
"Nephodia_auxesia,I_PBA5314.jpg",
"Leptostales_crossii,I_PBA24938.jpg",
"Glena_mopsaria,I_PBA6238.jpg",
"Hymenia_perspectalis,_Spotted_Beet_Webworm_Moth,I_PBA26845.jpg",
"Euglyphis_libnites,I_MFS548.jpg",
"Phyllodonta_latrata,I_PBA13647.jpg",
"Trygodes_amphion,I_PBA24048.jpg",
"Hampsonodes_mastoides,I_MFS1817.jpg",
"Glena_mopsaria,I_PBA23983.jpg",
"Glena_mopsaria,I_PBA31149.jpg",
"Hymenia_perspectalis,_Spotted_Beet_Webworm_Moth,I_PBA11757.jpg",
"Oospila_venezuelata,I_PBA32937.jpg",
"Crambidia_cephalica,I_PBA25573.jpg",
"Afrida_ydatodes,_Dyars_Lichen_Moth,I_PBA25475.jpg",
"Clemensia_brunneomedia,I_MFS10612.jpg",
"Glena_mopsaria,I_PBA33777.jpg",
"Micrathetis_dasarada,I_MFS13428.jpg",
"Nemoria_vermiculata,I_PBA8513.jpg",
"Clemensia_cincinnata,I_MFS10414.jpg",
"Thysanopyga_carfinia,I_MFS2278.jpg",
"Phyllodonta_latrata,I_PBA18934.jpg",
"Micrathetis_dasarada,I_MFS14179.jpg",
"Patalene_aenetusaria,I_PBA10553.jpg",
"Lophosis_labeculata,_Stained_Lophosis_Moth,I_MFS14970.jpg",
"Rhabdatomis_laudamia,I_PBA26106.jpg",
"Metanema_bonadea,I_MFS13161.jpg",
"Nemoria_vermiculata,I_PBA28175.jpg",
"Phalaenophana_pyramusalis,_Dark-Banded_Owlet_Moth,I_MFS11127.jpg",
"Antiblemma_pira,I_PBA23643.jpg",
"Clemensia_cincinnata,I_PBA12612.jpg",
"Oxydia_trychiata,I_MFS12818.jpg",
"Oospila_venezuelata,I_PBA23024.jpg",
"Nematocampa_arenosa,I_MFS13639.jpg",
"Nemoria_defectiva,I_PBA8787.jpg",
"Nemoria_defectiva,I_PBA28714.jpg",
"Amaxia_apyga,I_PBA24075.jpg",
"Nematocampa_completa,I_MFS8213.jpg",
"Hampsonodes_mastoides,I_MFS10997.jpg",
"Clemensia_leopardina,I_PBA28176.jpg",
"Hymenia_perspectalis,_Spotted_Beet_Webworm_Moth,I_PBA31257.jpg",
"Lobocleta_tenellata,I_PBA16776.jpg",
"Nephodia_auxesia,I_PBA30007.jpg",
"Anisoperas_atropunctaria,I_MFS6357.jpg",
"Cliniodes_opalalis,I_MFS6018.jpg",
"Semaeopus_viridiplaga,I_PBA29496.jpg",
"Pyrinia_selecta,I_PBA27174.jpg"]
input_csv = baseDir+ "classification_results.csv"  # Input CSV with predictions
output_csv = baseDir+"confusion_matrix_values_subset.csv"

# Read CSV file and process data
with open(input_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Get the header row
    
    # Identify column indices
    filename_idx = header.index("filename")
    # print(f"filename_idx is {filename_idx}")
    predicted_class_idx = header.index("Predicted class")
    # print(f"predicted_class_idx is {predicted_class_idx}")
    confidence_idx = header.index("Confidence")
    # print(f"confidence_idx is {confidence_idx}")
    labels = [col for col in header if col not in {"filename", "Predicted class", "Confidence"}]
    
    # Initialize counts
    stats = {label: defaultdict(int) for label in labels}
    
    for row in reader:
        if shouldUseOptionalList and row[filename_idx] not in optionalList:
            continue
        predicted_class = row[predicted_class_idx]
        print(f"predicted_class is {predicted_class}")
        
        for label in labels:
            print(f"current label is {label}")
            label_value = row[header.index(label)]
            print(f"label_value is {label_value}")
            true_label = label if label_value == "1" else None # @TODO don't think none should be the alternative
            print(f"true_label is {true_label}")
            
            if predicted_class == label:
                if true_label == label:
                    print(f"it's a true positive")
                    stats[label]["TP"] += 1  # True Positive
                else:
                    print(f"it's a false positive")
                    stats[label]["FP"] += 1  # False Positive
            else:
                if true_label == label:
                    print(f"it's a false negative")
                    stats[label]["FN"] += 1  # False Negative
                else:
                    print(f"it's a true negative")
                    stats[label]["TN"] += 1  # True Negative

# Write results to a new CSV file
with open(output_csv, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Label", "True Positives", "True Negatives", "False Positives", "False Negatives"])
    
    for label, counts in stats.items():
        writer.writerow([label, counts["TP"], counts["TN"], counts["FP"], counts["FN"]])

print(f"Confusion matrix saved to {output_csv}")
