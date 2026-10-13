Private data source transparency
2026-10-12
Private datasources are only required to be explained at a very high level in the public summary of training content. Nonetheless, we observe widespread noncompliance in existing summaries.
---

The public summary of training content requires providers to publish information regarding the private datasets used to train their model. This section requires relatively little disclosure, however does require answering some substantive questions about use of licensed data and other private data acquired through various means.

In this blog post, we outline key issues identified with regards to disclosure within this section across 62 public summaries of training data. Issues observed include failures to provide substantive descriptions of training data matching the desired level of detail of the template, incomplete content descriptions, declining to provide meaningful information, various deviations from the desired structure, fuzzy definitions of ‘licensing’, and various problems resulting from models with (likely) meaningfully different training data being listed in the same summary. It is our hope that this blog post can be used by providers to strengthen their own summaries and to arrive at a high-scoring template. Simultaneously, we point out key issues in order to alert regulators to the fact that even in a section where relatively little information needs to be provided, we still see large amounts of avoision behaviour.

## TL;DR

| \# | Model |
| ----: | :---- |
| 1 | Baguettotron and Monad |
| 2 | Pleias 1.0 |
| 3 | Apertus |
| 4 | Luciole Base |
| 5 | FIBO |
| 6 | Bria 3.2 |
| 7 | Luciole Instruct 1.1 |
| 8 | SmolLM3-3B |
| 9 | Domyn Large |
| 10 | Bielik v3 11B Instruct |
| 11 | PLLuM-12B-base-2512 |
| 12 | Adobe Firefly |
| 13 | Nemotron 3 and 3.5 Family |
| 14 | Inkling |
| 15 | Inkling Small |
| 16 | FLUX.3 |
| 17 | Nova 2 Lite |
| 18 | Nemotron Nano 12B v2 |
| 19 | FastwebMIIA |
| 20 | MAI Cyber 1 Flash |
| 21 | MAI Code 1.1 Flash |
| 22 | Minimax M3 |
| 23 | MAI Code 1 Flash |
| 24 | MAI-Image-2.5 |
| 25 | Ministral 3 14B |
| 26 | Ministral 3 8B |
| 27 | Ministral 3 3B |
| 28 | MAI-Image-2 |
| 29 | GPT-5.6 Luna |
| 30 | Apertus v1.5 |
| 31 | GPT-5.5 |
| 32 | GPT-6 Astra |
| 33 | GPT-5.2 |
| 34 | GPT-5.4 Nano |
| 35 | GPT Images 2.0 |
| 36 | Grok 4.5 |
| 37 | Grok Voice Think Fast 2.0 |
| 38 | Hy3 |
| 39 | Gemma 4 |
| 40 | Gemini 3 Pro |
| 41 | Mistral Small 4 |
| 42 | Mistral Large 3 |
| 43 | Mythos 5.1 / Fable 5.1 |
| 44 | Command A+ |
| 45 | Claude Opus 5 |
| 46 | Claude Opus 4.8 |
| 47 | Claude Mythos 5 / Claude Fable 5 |
| 48 | Claude Mythos Preview |
| 49 | Claude Sonnet 5 |
| 50 | Claude Opus 4.7 |
| 51 | Muse Image |
| 52 | Muse Glimmer |
| 53 | Muse Spark |
| 54 | Phi 4 Reasoning Vision 15B |
| 55 | Seed 2.0 Pro |
| 56 | Seedance 2.5 |
| 57 | Seedance 2.0 |
| 58 | Seedream 5.0 Pro |
| 59 | Midjourney Image and Video family |
| 60 | DeepSeek-V4 |
| 61 | Phi-4 |

| \# | Identified issue |
| ----: | :---- |
| **1.1** | Failures to provide substantive descriptions of private data: descriptions of acquisition agreements in place of describing data contents |
| **1.2** | Failures to provide substantive descriptions of private data: generic references to key data aspects (“domains”, “contexts”, etc.) |
| **1.3** | Failures to provide substantive descriptions of private data: rights-management description instead of dataset description |
| **2.1** | Incomplete description of contents: missing information about the nature of contents |
| **2.2** | Incomplete description of contents:Missing linguistic characteristics |
| **2.3** | Incomplete description of contents:Missing information about modalities |
| **3.1** | Vaguely declining to provide a substantive answer: Through use of ‘N/A’ |
| **3.2** | Vaguely declining to provide a substantive answer: Missing dataset versions / explanations, missing references to further information |
| **3.3** | Vaguely declining to provide a substantive answer: Missing fields |
| **4.1** | Structure deviations: ‘Other’ options |
| **4.2** | Structure deviations: Field collapse |
| **4.3** | Structure deviations: Information which should be provided elsewhere |
| **5.1** | ‘Licensing’ definitions: Inconsistent use of licensing terminology |
| **6.1** | Model granularity: What happens when a single summary is provided for meaningfully different models? |
| **6.2** | Model granularity: No base model indicated |

| \# | 1.1 | 1.2 | 1.3 | 2.1 | 2.2 | 2.3 | 3.1 | 3.2 | 3.3 | 4.1 | 4.2 | 4.3 | 5.1 | 6.1 | 6.2 | 7.1 |
| ----: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |
| 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |
| 5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |
| 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  |
| 12 |  |  |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |
| 13 |  |  |  |  | ✓ |  |  | ✓ |  |  |  |  | ✓ |  | ✓ |  |
| 14 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 15 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 16 | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 17 |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |
| 18 |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 21 |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 22 |  |  |  |  | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 23 |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 24 |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| 25 | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 26 | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 27 | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 28 |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| 29 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
| 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
| 32 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
| 33 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
| 34 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
| 35 |  |  |  |  |  |  |  |  |  | ✓ |  | ✓ |  |  |  |  |
| 36 |  | ✓ |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |  |
| 37 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 38 |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 39 |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 40 |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 41 | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 42 | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  |  |
| 43 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 44 |  |  |  |  |  |  |  |  | ✓ |  |  | ✓ |  |  |  |  |
| 45 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 46 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 47 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 48 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 49 |  | ✓ |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |  |
| 50 |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  |
| 51 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 52 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 53 |  |  |  |  | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 54 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 |  |  |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 56 |  |  |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 57 |  |  |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 58 |  |  |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 59 | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  |  |  | ✓ |  |  |
| 60 |  | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  |  |  |  |
| 61 |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  |  |

## Failures to provide substantive descriptions of private data

### Descriptions of acquisition agreements in place of describing data contents

_Observed in: FLUX.3; Ministral 3 14B; Ministral 3 8B; Ministral 3 3B; Mistral Small 4; Mistral Large 3; Midjourney Image and Video family_

In the field asking for a general description of non-publicly known private datasets obtained from third parties, we observe several model summaries which describe data acquisition agreements instead of data contents. This is despite the field explicitly asking for the description of data. The FLUX.3 model, for instance, only describes its data as “Data acquired from third party providers through confidential commercial agreements and data access partnerships. Data is collected consistent with applicable law.” This description is not a relevant description of the contents of the data themselves, and only signals that (presumably not commercially-licensed) agreements are in place.

Similarly, the corresponding description for Mistral 4 Small states that “Mistral AI works with a variety of third-party providers for access to synthetically generated and human-curated datasets. These datasets are obtained and curated using industry-standards and accessed under commercial or partnership agreements with the relevant contractual guarantees.” While this does specify that the data is synthetically generated and human-curated, beyond this it only provides information about the agreement in place.

Lastly, the summary for the Midjourney family of models provides its description as “Data is covered by agreements that outline the party’s roles and responsibilities with respect to the datasets Midjourney uses.” This is similar to the description for FLUX.3 in only providing a brief description of the agreement, albeit in this case not even providing the impression that the reason information cannot be disclosed is due to confidentiality.

The field in which descriptions of data have to be provided is unambiguous in its ask for a description of the data. This is not an ask which is difficult to comply with, as other providers which do provide a substantive summary in this section confirm. We encourage providers who instead provide a description of data agreements to update their summaries to accurately reflect data contents.

### Generic references to key data aspects (“domains”, “third-party-data”, “contexts”)

_Observed in: GPT-5.6 Luna, GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano; Grok 4.5; Mythos 5.1 / Fable 5.1, Claude Opus 5, Claude Opus 4.8, Claude Mythos 5 / Claude Fable 5, Claude Mythos Preview, Claude Sonnet 5, Claude Opus 4.7; DeepSeek-V4_

In the same field, we see many occurrences of organizations referring to data contents through generic descriptors. For instance, an organisation may state that it includes data “spanning a diverse set of domains and contexts” (Grok 4.5) rather than enumerating what these domains and contexts are. Or an organisation may provide its description as “The dataset is mainly composed of text data sourced from multiple domains.” (DeepSeek-V4). Such descriptions provide so little information as to be essentially meaningless, and as such do not adhere to the goals of the public summary as a document which empowers rightsholders.

### Rights management description in place of dataset description

_Observed in: FLUX.3; MAI Cyber 1 Flash, MAI Code 1.1 Flash, MAI Code 1 Flash; Midjourney Image and Video family_

Lastly, we observe some instances of the general description of non-publicly known private datasets obtained from third parties instead describing the way rights were managed in the data. For instance, the summary for the Midjourney Image and Video family provides as a description “Data is covered by agreements that outline the party’s roles and responsibilities with respect to the datasets Midjourney uses.” This entirely pertains to the data agreements in which Midjourney engages rather than the contents of the data. Similarly, the summary for MAI Code 1.1 Flash states that “Acquired text data is vetted for compliance with use rights, applicable data privacy and security laws, and is covered by agreements describing the roles and responsibilities of the parties with respect to the data.” This restricts the description to talking about rights management.

## Incomplete description of contents

In order to measure the completeness of the description of non-publicly known private datasets obtained from third parties, we measure the inclusion of three separate kinds of content, as based on the template's suggested text encouraging the mention of all three. These three aspects are the nature of the contents of the datasets, their linguistic characteristic, and their modalities. The models in which each were observed to be missing are the following:

- **Missing information about nature of contents:** FLUX.3; MAI Cyber 1 Flash, MAI Code 1.1 Flash, MAI Code 1 Flash; Ministral 3 14B, Ministral 3 8B, Ministral 3 3B, GPT-5.6 Luna, GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano; Grok 4.5; Mistral Small 4, Mistral Large 3; Mythos 5.1 / Fable 5.1, Claude Opus 5, Claude Opus 4.8, Claude Mythos 5 / Claude Fable 5, Claude Mythos Preview, Claude Sonnet 5, Claude Opus 4.7; Seed 2.0 Pro, Seedance 2.5, Seedance 2.0, Seedream 5.0 Pro; Midjourney Image and Video family; DeepSeek-V4  
- **Missing information about linguistic characteristics:** Nemotron 3 and 3.5 Family; Inkling, Inkling Small; FLUX.3; Nemotron Nano 12B v2; MAI Cyber 1 Flash, MAI Code 1.1 Flash; Minimax M3; MAI Code 1 Flash; MAI-Image-2.5; Ministral 3 14B, Ministral 3 8B, Ministral 3 3B; MAI-Image-2; GPT-5.6 Luna; GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano; Grok 4.5, Grok Voice Think Fast 2.0; Gemma 4, Gemini 3 Pro; Mistral Small 4, Mistral Large 3; Mythos 5.1 / Fable 5.1, Claude Opus 5, Claude Opus 4.8, Claude Mythos 5 / Claude Fable 5, Claude Mythos Preview, Claude Sonnet 5, Claude Opus 4.7; Muse Image, Muse Glimmer, Muse Spark; Seed 2.0 Pro, Seedance 2.5, Seedance 2.0, Seedream 5.0 Pro; Midjourney Image and Video family; DeepSeek-V4  
- **Missing information about modalities:** FLUX.3; Nova 2 Lite; Nemotron Nano 12B v2; MAI Cyber 1 Flash, MAI Code 1.1 Flash; Minimax M3; MAI Code 1 Flash; Ministral 3 14B, Ministral 3 8B, Ministral 3 3B; GPT-5.6 Luna, GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano; Hy3; Gemma 4, Gemini 3 Pro; Mistral Small 4, Mistral Large 3; Mythos 5.1 / Fable 5.1, Claude Opus 5, Claude Opus 4.8, Claude Mythos 5 / Claude Fable 5, Claude Mythos Preview, Claude Sonnet 5, Claude Opus 4.7; Midjourney Image and Video family; Phi-4

The lack of a description of these characteristics means those cannot be used as evidence for the inclusion of potential rights violations. This is particularly pertinent in the case of missing linguistic characteristics, as several data sovereignty agreements are in place for languages such as Māori. In this sense, the potential application of description of linguistic characteristics has a potential scope beyond the European one.

## Vaguely declining to provide a substantive answer

### Through use of ‘N/A’

_Observed in: Adobe Firefly, Inkling, Inkling Small; FLUX.3; Nemotron Nano 12B v2; Minimax M3; Ministral 3 14B, Ministral 3 8B, Ministral 3 3B; GPT-5.6 Luna, GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano; Grok Voice Think Fast 2.0; Hy3; Gemma 4, Gemini 3 Pro; Mistral Small 4, Mistral Large 3; Claude Opus 4.7; Muse Image, Muse Glimmer, Muse Spark; Seed 2.0 Pro, Seedance 2.5, Seedance 2.0, Seedream 5.0 Pro; DeepSeek-V4_

Many summaries have been observed to decline substantive answers through the use of ‘N/A’. This can easily lead to unclarities about the reason for why the provider believes the relevant field does not apply. For instance, Adobe Firefly responds to the question asking to provide a list of private datasets obtained from other third parties with “N/A”. In this case, it is ambiguous whether Adobe seeks to indicate that none of the private datasets obtained from other third parties are publicly known, or that they do not consider the field otherwise applicable. As such a rightsholder has no way of ascertaining for certain whether Adobe used private datasets which satisfy the criteria of this field. This hurts the amount of disclosure in the response. Muse Glimmer, similarly, leaves the corresponding field blank.

We encourage providers to explicitly enumerate the criteria for including datasets in certain fields. For instance, in the case of Adobe Firefly the provider could explicitly indicate that “We do not believe that any private datasets obtained from other third parties are publicly known.” If they believe that this is the case.

### Missing dataset versions/explanations, missing references to further information

_Observed in: Nemotron 3 and 3.5 Family_

In the only summary which has provided a list of datasets in its answer to “If publicly known, list private datasets obtained from other third parties”, the summary was not found to disclose any dataset versions and explanations, nor references to further information. By instead only naming the datasets themselves, the summary makes it so that rightsholders are not able to determine as easily what datasets the provided identifiers refer to, and in the cases where rightsholders only have certain information in specific versions of the dataset they are unable to determine whether those specific versions ended up in the final model.. The downstream harms of disclosure in this manner are obvious, and so we would encourage providers to be more forthcoming in this manner.

### Missing fields

_Observed in: Adobe Firefly_

Lastly, we observe some summaries which miss key fields altogether. This is the case with Adobe Firefly, where no general description of non-publicly known private datasets obtained from third parties is provided.

## Structure deviations

### ‘Other’ options

_Observed in: Minimax M3; Ministral 3 14B, Ministral 3 8B, Ministral 3 3B; GPT-5.6 Luna; GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano, GPT Images 2.0; Mistral Small 4, Mistral Large 3; Command A+_

We observe several instances of providers modifying the template to include an ‘other’ option in ‘yes’ or ‘no’ fields. Arguments towards including such a field run both ways. On the one hand, it can be argued that the information desired by the section (licensed data) is too complex to be answered by a simple binary. On the other hand, going beyond the template risks introducing additional unclarities.

### Field collapse

_Observed in: Domyn Large_

In the summary for Domyn Large, we observe the merging together of several fields. This can introduce additional unclarities in the template through deviations from the intended structure. While merging of fields may be desirable in limited circumstances from the perspective of a model developer, especially when individual fields do not provide much information, we generally caution against it to ensure good interpretability of individual summaries.

### Information which should be provided elsewhere

_Observed in: GPT-5.6 Luna, GPT-5.5, GPT-6 Astra, GPT-5.2, GPT-5.4 Nano, GPT Images 2.0_

We observe several models which provide information which should be provided elsewhere. For instance, the summary for GPT-5.6 Luna states in the field “General description of non-publicly known private datasets obtained from third parties” that “OpenAI partnered with third parties to access data spanning a diverse set of domains and contexts to improve GPT-5.6 Luna. Data is accessed in compliance with applicable laws.” This is not relevant for the given field, and provides information (that data is accessed in compliance with applicable laws) which should be provided in fields talking about rights compliance.

## ‘Licensing’ definitions

### Inconsistent use of licensing terminology

_Observed in: Nemotron 3 and 3.5 Family; Command A+_

We observe several datasets listed by the Nemotron 3 and 3.5 Family summary which arguably do not belong in the field. For instance, SIFT-50M likely does not need to be indicated as a private dataset, as it is freely licensed and seems to be sourced only from publicly accessible data. Similarly, the Granary dataset also likely does not need to be indicated here, though with NVIDIA being the creator and sourcing its data partially from claimed Youtube Commons, it might be the case that some private data was found to be present. Command A+, meanwhile confuses fields 2.2.2 and 2.2.1, explicitly indicating that they include some commercially licensed datasets in the former field. Neither behavior is desirable from a clarity perspective.

## Incorrect fields

### Inconsistent modalities

_Observed in: FIBO, Bria 3.2_

In the summaries of FIBO and Bria 3.2, we observe an inconsistency between the sources of private data indicated in the private datasets section and those in the general model details section. The model only indicates use of image data from private datasets, however in its general information states that both text and image data is used. The likely cause of this inconsistency is the question of whether to take image captions as ’text’ data or to consider them part of ‘image’ data. We believe that both modalities should be mentioned, however we also encourage further clarity for this in the template.

## Model granularity

### What happens when a single summary is provided for meaningfully different models?

_Observed in: PLLuM-12B-base-2512; Midjourney Image and Video family_

We observe several summaries which include models with (likely) meaningfully different training data. This is opposed to point (30) of the Explanatory Notice included alongside the template, which states that “The same Summary may be used for different models or different model versions if the content of their respective Summaries is identical.” Including multiple models with different training data in a single summary risks introducing significant unclarities into the summary, as it becomes very difficult to assess, for instance, whether certain training data was included in one model but not the other or whether data used to train a certain model was left out.

For instance, take the summary for PLLuM-12B-base-2512. This summary includes the Gemma-based PLLuM-4B-base-2512, the Llama-based Llama-PLLuM-8B-base-2512, and the Mistral-Nemo-based PLLuM-12B-base-2512. Each of these models originates from a separate large pretraining run, and so summaries should be published separately. In fact, an argument may be made that none of these models require a public summary of training content as each originates from a large pretraining run with far more than a third of the compute expended than was used for fine-tuning (point (60) in the Commission Guidelines on the scope of the obligations for providers of general-purpose AI models).

We see similar aggregation in the Midjourney Image and Video family of models. This summary includes both text-to-image and (text)-image-to video models, which are delivered separately by Midjourney.

### No base model indicated

_Observed in: Nemotron 3 and 3.5 Family_

In the case of the summary for the Nemotron 3 and 3.5 family of models, we observe that the summary is strictly only claimed for the quantifications of the model. The model provider also does not indicate any models on which the model was trained. This is despite different versions of the model family being published separately on HuggingFace. Although this represents only a relatively minor drafting error, as the inference can easily be made that the summary is intended to also cover the other models which are part of the same large pretraining run, this is still something which should be clarified.

## Conclusion

In general, we see issues both in providers providing too little information, declining to publish information which is recommended by the template, and with providers providing information in a manner which introduces additional unclarities. It is our hope that providers are able to utilize the lessons outlined in this blog post in order to further improve their summaries, and create compliant new ones.