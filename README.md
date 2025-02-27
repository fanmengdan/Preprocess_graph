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