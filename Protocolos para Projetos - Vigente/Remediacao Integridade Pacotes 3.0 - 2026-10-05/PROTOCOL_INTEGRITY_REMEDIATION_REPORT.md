# PROTOCOL_INTEGRITY_REMEDIATION_REPORT

STATUS = BLOCKED
ACTIVITY_COMPLETION_PERCENT = 95%
COMPLETION_BASIS = The 17 manifest-governed files were restored to the byte representation whose SHA-256 and size match the original manifests. Both rebuilt ZIPs were freshly extracted and all 17 hashes and sizes match. Schema JSON parsing and all 9 local $ref pointers pass, but full Draft 2020-12 schema validation could not be run because no compatible validator is available. The Continuity manifest also labels PM-02 R2.5 and PM-03 R2.2 active, while the current Matrix Registry lists PM-02 1.7-R2.6 and PM-03 1.7-R2.3. Those normative references were preserved.

INTEGRITY_ROOT_CAUSE = LINE_ENDING_ONLY
OPENING_PROTOCOL_INTEGRITY = PASS for manifest hash, size, and fresh extraction checks; package adoption remains BLOCKED by the global schema and stale dependency review gates.
CONTINUITY_PROTOCOL_INTEGRITY = PASS for manifest hash, size, and fresh extraction checks; package adoption remains BLOCKED by the global schema and stale dependency review gates.
NORMATIVE_CONTENT_CHANGED = NO
FILES_CHECKED = 19 ZIP entries total (17 manifest-governed files plus two manifests); the 17 governed files were compared in representations A/B/C.
FILES_REMEDIATED = 17 governed payload/schema files reconstructed using LF bytes; both manifests were packaged with LF line endings and their values unchanged.
MANIFEST_HASH_CHECK = 17/17
MANIFEST_SIZE_CHECK = 17/17
CANONICAL_TEXT_BYTE_FORMAT = LF
CANONICALIZATION_BASIS = In every one of the 17 entries, source bytes were CRLF; CRLF-to-LF bytes matched the original declared SHA-256 and size exactly; decoded text was equivalent. LF-to-CRLF and source bytes did not match. Cause location before receipt cannot be determined from available evidence.
MANIFEST_REBUILT = NO manifest values changed; original file lists, hashes, and sizes were retained.
POST_PACKAGE_EXTRACTION_CHECK = PASS for both fresh extractions.
SCHEMA_VALIDATION = BLOCKED: schema parses as JSON; draft declares 2020-12; 9/9 local refs resolve; no installed validator performed full Draft 2020-12 validation. PowerShell Test-Json rejected a valid 2020-12 const probe and was excluded as incompatible.
INTERNAL_REFERENCE_CHECK = PASS: Opening sibling Continuity package and referenced schema exist; schema local refs 9/9 resolve; Markdown relative-link scan found no Markdown-style local links to check and no broken links.

## Package results

PACKAGE = PROJECT_OPENING 3.0
ROOT_CAUSE = LINE_ENDING_ONLY
FILES_CHECKED = 13 governed files
FILES_REMEDIATED = 13
NORMATIVE_CONTENT_CHANGED = NO
CANONICAL_BYTE_FORMAT = LF
MANIFEST_REBUILT = NO value changes; line endings canonicalized
POST_PACKAGE_HASH_CHECK = 13/13 PASS
POST_PACKAGE_SIZE_CHECK = 13/13 PASS
SCHEMA_VALIDATION = BLOCKED by Continuity Draft 2020-12 validator unavailability
INTERNAL_REFERENCE_CHECK = PASS for sibling Continuity package and referenced schema presence
RESULT = BLOCKED pending schema and stale dependency review gates
FINAL_ZIP = C:\Users\walacedelgado\PycharmProjects\governanca_de_projetos\Protocolos para Projetos - Vigente\Remediacao Integridade Pacotes 3.0 - 2026-10-05\PROJECT_OPENING_3.0-REMEDIATED-MANIFEST-MATCHED.zip
FINAL_ZIP_SHA256 = 737be69e02819eff07ce68de22d1872bc0d6489e47d6ffcab87b2662fe795914
FINAL_ZIP_SIZE = 23351 bytes

PACKAGE = CONTINUITY 3.0
ROOT_CAUSE = LINE_ENDING_ONLY
FILES_CHECKED = 4 governed files
FILES_REMEDIATED = 4
NORMATIVE_CONTENT_CHANGED = NO
CANONICAL_BYTE_FORMAT = LF
MANIFEST_REBUILT = NO value changes; line endings canonicalized
POST_PACKAGE_HASH_CHECK = 4/4 PASS
POST_PACKAGE_SIZE_CHECK = 4/4 PASS
SCHEMA_VALIDATION = BLOCKED: JSON parse PASS, draft identified as 2020-12, internal refs 9/9 PASS; full Draft 2020-12 validation unavailable
INTERNAL_REFERENCE_CHECK = PASS: all 9 local schema refs resolve
RESULT = BLOCKED pending schema and stale dependency review gates
FINAL_ZIP = C:\Users\walacedelgado\PycharmProjects\governanca_de_projetos\Protocolos para Projetos - Vigente\Remediacao Integridade Pacotes 3.0 - 2026-10-05\CONTINUITY_3.0-REMEDIATED-MANIFEST-MATCHED.zip
FINAL_ZIP_SHA256 = 430d3671826a7e1887a7282cf966869c9d74cc5f7382c5b9c6767eaf09fb8e2e
FINAL_ZIP_SIZE = 10010 bytes

## Cross-protocol and policy reference check

Opening 3.0 points to sibling Continuity 3.0 and its schema; both paths resolve in the supplied governance package location.
The supplied current Matrix POLICY_REGISTRY.json declares PM-02 1.7-R2.6 and PM-03 1.7-R2.3 as canonical active versions. Continuity 3.0 declares PM-02 R2.5 and PM-03 R2.2 as canonical active dependencies.
Classification: PM-02 R2.5 and PM-03 R2.2 = STALE_REFERENCE_REQUIRING_REVIEW. No dependency string, policy, protocol, or manifest value was edited. A normative review is required before treating Continuity as an adoptable active authority.

## Integrity evidence

For each of the 17 manifest-listed files, the attached CSV and JSON record expected manifest SHA-256 and size, actual source SHA-256 and size, normalized LF and CRLF representations, decoded text equivalence, and canonicalized result. Every LF-normalized SHA-256 and byte count matches the manifest.

Opening source ZIP SHA-256 = ae6d1f9d0d97b9c8f3a0d0395f76603488f9580278cc733928981d29e7397b49
Continuity source ZIP SHA-256 = bc3c9629e21f260e4bd95844354734ae2b349ba03f3e4c8a336dc4a0967aa3fb
FINAL_OPENING_ZIP_SHA256 = 737be69e02819eff07ce68de22d1872bc0d6489e47d6ffcab87b2662fe795914
FINAL_CONTINUITY_ZIP_SHA256 = 430d3671826a7e1887a7282cf966869c9d74cc5f7382c5b9c6767eaf09fb8e2e
ALL_MANIFEST_HASHES_MATCH = YES
ALL_MANIFEST_SIZES_MATCH = YES
POST_ZIP_EXTRACTION_CHECK = PASS
UNRESOLVED_BYTE_DIVERGENCE = 0 within manifest-governed files
UNRESOLVED_CONTENT_DIVERGENCE = 0

## Artifacts and remaining work

FILES_CREATED = two separately named remediated ZIPs, this report, protocol-integrity-remediation-evidence.json, protocol-integrity-file-matrix.csv, and clean post-extraction audit folders.
FILES_UPDATED = No original source archives, policies, or Telegram project files were changed. New review artifacts are saved in the remediation output folder.
FINDINGS = All 17 mismatches were only CRLF/LF representation differences. Manifest values are evidence-supported and unchanged. Original source ZIP hashes were recorded above.
BLOCKERS = No available runtime has a Draft 2020-12 validator; stale active PM-02 and PM-03 references need normative review.
NEXT_REQUIRED_ACTIVITY = Run the schema and representative binding instances through an approved Draft 2020-12 validator, then resolve PM-02/PM-03 reference versions through a separate normative review before adopting these packages.

The remediation candidate ZIPs pass manifest hashes, sizes, and fresh extraction checks. Overall STATUS remains BLOCKED because the required schema validation and authority-reference review are incomplete.

REISSUED_DELIVERY_FOLDER = C:\Users\walacedelgado\PycharmProjects\governanca_de_projetos\Protocolos para Projetos - Vigente\Remediacao Integridade Pacotes 3.0 - 2026-10-05
The five deliverable files in this folder are byte-identical to the reissued files. The original source ZIPs remain unchanged. 

