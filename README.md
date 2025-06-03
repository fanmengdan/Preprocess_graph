 <div align="center">
  <h1 id="Preprocess Graph"><a href="https://gitee.com/fanmengdan1/preprocess_graph_mac/" target="repo">Preprocess Graph</a></h1>
</div>

#### This code aims at preprocessing the information of *entity reference graph* and *code change graph* to adjacency matrix that a GNN can learn.

## Requirements
- macOS/Windows/Linux
- anaconda (python 3.7)
- networkx

## Usage
### 1. Get different information file paths of all composite commits.
 - **getVertexPath.py:**
   Get vertex files *(indicates source and target entities of each edge)* paths of all composite commits.
 - **getVertexTypePath.py:**
   Get vertex type file *(indicates type of each entity)* paths of all composite commits.
 - **getGTPath.py:**
   Get ground truth file *(indicates the each code change in which atomic commit)* paths of all composite commits.

### 2. Map the complex ID of code changes to order numbers.
 - **ExtractHunkList.py:**
   Get ground truths. **Each code change is marked with a complex ID**
 - **HunkIDmap.py**
   Map the  complex ID of each code change (Hunk) to a order number.
 - **MapHunkID2Num.py**
   For ground truths, remarked the code changes with their order numbers.
   
  ### 3. Encode types of entities to order numbers.
  
  **EncodeVertexAttribute.py:**
  Each type of entitiy is encoded to a number. The number is regarded as the attribute of the entity.
   
### 4. Get adjacency matrixs of graphs that a GNN can learn.
 - **BuildEntityGraph.py:** 
    For entity reference graphs, we use **networkx** first build *entity reference graphs* according the vertex files *(indicates source and target entities of each edge)* and vertex type files *(indicates type of each entity)*, and then get the adjacency matrixs **(among them, each edge is represented by the attribute value (number) of the edge type)** of *entity reference graphs*.
 - **BuildHunkGraph.py:**
	For code change graph, according the ground truths, we create edges by fully connecting all code changes in each atomic commit, and then get the adjacency matrixs of *code change graphs*.

### 5. Padding and cutting Adjs
**Padding.py：**
Pad all Adjs into the same shape.
**Cutting.py:**
Cut all Adjs into the same shape.



## Datasets

The dataset is in the `HD-GNN` folder, which contains the information of entity reference graph and code change graph of each tangled commit. 

As described in section 5.2 of the accepted paper, we used a common dataset. Each composite/tangled commit in this dataset is composed of 2/3/5 atomic commits. 

Directory structure:
- `HD-GNN/dataset/glide/2/` - Tangled commits each consisting of 2 atomic commits
- `HD-GNN/dataset/glide/3/` - Tangled commits each consisting of 3 atomic commits  
- `HD-GNN/dataset/glide/5/` - Tangled commits each consisting of 5 atomic commits

Each subfolder (e.g., `0bdf6a7_928c9a1` in `HD-GNN/dataset/glide/5/`) contains the ground truth files for that tangled commit (composed of commits 0bdf6a7 and 928c9a1 in this example).

Example files in each commit folder:
- **GT_0bdf6a7_928c9a1.txt** - The ground truth. Records the code change included by each atomic commit using their IDs.
- **Id_0bdf6a7_928c9a1.txt** - The entity ID information. Records entities of the tangled commit using their IDs.  
- **Type_0bdf6a7_928c9a1.txt** - The entity type information. Records type of each entity in the tangled commit.
- **Index_0bdf6a7_928c9a1.txt** - The index information. Records which code changes contain each entity using their IDs.
- **Source_0bdf6a7_928c9a1.txt** - The syntactic relation information. Records the source entity of each syntactic relation.
- **Target_0bdf6a7_928c9a1.txt** - The syntactic relation information. Records the target entity of each syntactic relation.

The meaning of other data files follows the same pattern.
