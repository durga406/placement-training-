int majorityElement(int* nums, int numsSize) {
    int sol=nums[0],col=0;
    for(int i=0;i<numsSize;i++){
        if(col==0){
            sol=nums[i];
        }
        if(sol==nums[i]){
            col++;
        }
        else{
            col--;
        }
    }
    return sol;
}
