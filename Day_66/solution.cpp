class Solution {
  public:
    // Function to delete a node from BST.
    Node* deleteNode(Node* root , int target){
        if (!root){
            return NULL;
        }
        if (target < root->data){
            root->left = deleteNode(root->left,target);
            return root;
        }
        else if (target > root->data){
            root->right = deleteNode(root->right,target);
            return root;
        }
        else { // target == root->data
            
            
            //leaf node
            if(!root->left&&!root->right){
                delete root;
                return NULL;
            }
            else if(!root->right){//only left child exist
                Node* temp = root->left;
                delete root;
                return temp; 
            }
            else if(!root->left){// only right child exists
                Node* temp = root->right;
                delete root;
                return temp; 
            } 
            //two child exists
            else{
                // find the greatest element from the left
                Node* parent = root;
                Node* child = root->left;
    
                //rightmost node tak pochna hai left side wale
                while(child->right){
                    parent=child;
                    child= child->right;
                }
    
                if (root!=parent){
                    parent->right=child->left;
                    child->left= root->left;
                    child->right= root->right;
                    delete root;
                    return child;
                }
                else{
                    child->right=root->right;
                    delete root;
                    return child;
                }
            
            
            
            }
    
        }   
    }
};
