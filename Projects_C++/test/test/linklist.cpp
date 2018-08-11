template<class T>
class slistNode
{
    public:
    slistNode(){next=NULL;}
    T data;//ֵ
    slistNode* next;//ָ����һ���ڵ��ָ��
};
template<class T>
class myslist
{
    private:
    unsigned int listlength;
    slistNode<T>* node;//��ʱ�ڵ�
	slistNode<T>* headnode;//ͷ�ڵ�
    slistNode<T>* lastnode;//β���
    public:
        myslist();//��ʼ��
        unsigned int length();//����Ԫ�صĸ���
        void add(T x);//��β���Ԫ��
        void traversal();//��������������ӡ
        bool isEmpty();//�ж������Ƿ�Ϊ��
        slistNode<T>* find(T x);//����ֵΪx�Ľڵ�,���ؽڵ�ĵ�ַ,�Ҳ�������NULL
        void Delete(T x);//ɾ��ֵΪx�Ľڵ�
        void insert(T x,slistNode<T>* p);//��p�ڵ�����ֵΪx�Ľڵ�
        void insertHead(T x);//�������ͷ������ڵ�

};
template<class T>
myslist<T>::myslist()
{
    node=NULL;
    lastnode=NULL;
    headnode=NULL;
    listlength=0;
}
template<class T>
inline unsigned int myslist<T>::length(){return listlength;}

template<class T>
void  myslist<T>::add(T x)
{
    node=new slistNode<T>();//����һ���µĽڵ�
    node->data=x;//�½ڵ㸳ֵΪx
    if(lastnode==NULL)//���û��β�ڵ�������Ϊ��,node��Ϊͷ���,����β�ڵ�
    {
        headnode=node;
        lastnode=node;
    }
    else//�������ǿ�
    {
        lastnode->next=node;//node��Ϊβ�ڵ����һ���ڵ�
        lastnode=node;//node�����β�ڵ�,��β�ڵ㸳ֵΪnode
    }
    ++listlength;//Ԫ�ظ���+1
}

template<class T>
void  myslist<T>::traversal()
{
    node=headnode;//����ʱ�ڵ�ָ��ͷ���
    while(node!=NULL)//�����������
    {
        cout<<node->data<<ends;
        node=node->next;
    }
    cout<<endl;
}
template<class T>
bool  myslist<T>::isEmpty()
{
    return listlength==0;
}
template<class T>
slistNode<T>* myslist<T>::find(T x)
{
    node=headnode;//����ʱ�ڵ�ָ��ͷ���
    while(node!=NULL&&node->data!=x)//��������,����ֵ��ͬ�Ľڵ�����
    {
        node=node->next;
    }
    return node;//�����ҵ��Ľڵ�ĵ�ַ,���û���ҵ��򷵻�NULL
}
template<class T>
void  myslist<T>::Delete(T x)
{
    slistNode<T>* temp=headnode;//����һ����ʱ�ڵ�ָ��ͷ�ڵ�
    if(temp==NULL) return;//���ͷ�ڵ�Ϊ��,���������Ԫ��,ֱ�ӷ���
    if(temp->data==x)//���ͷ�ڵ��ֵΪҪɾ����ֵ,��ɾ��Ͷ�ڵ�
    {
        headnode=temp->next;//��ͷ�ڵ�ָ��ͷ�ڵ����һ���ڵ�
        if(temp->next==NULL) lastnode=NULL;//���������ֻ��һ���ڵ�,ɾ��֮���û�нڵ���,��β�ڵ���Ϊ��
        delete(temp);//ɾ��ͷ�ڵ�
        return;
    }
    while(temp->next!=NULL&&temp->next->data!=x)//���������ҵ���һ��ֵ��x��ȵĽڵ�,temp��ʾ����ڵ����һ���ڵ�
    {
        temp=temp->next;
    }
    if(temp->next==NULL) return;//���û���ҵ��򷵻�
    if(temp->next==lastnode)//����ҵ���ʱ��β�ڵ�
    {
        lastnode=temp;//��β�ڵ�ָ��������һ���ڵ�
        delete(temp->next);//ɾ��β�ڵ�
        temp->next=NULL;
    }
    else//�������β�ڵ�
    {
        node=temp->next;//����ʱ�ڵ�nodeָ��Ҫɾ���Ľڵ�
        temp->next=node->next;//Ҫɾ���Ľڵ����һ���ڵ�ָ��Ҫɾ���ڵ����һ���ڵ�
        delete(node);//ɾ���ڵ�
        node=NULL;
    }
}
template<class T>
void  myslist<T>::insert(T x,slistNode<T>* p)
{
    if(p==NULL) return;
    node=new slistNode<T>();//����һ���µĿռ�
    node->data=x;
    node->next=p->next;
    p->next=node;
    if(node->next==NULL)//���nodeΪβ�ڵ�
    lastnode=node;
}
template<class T>
void  myslist<T>::insertHead(T x)
{
    node=new slistNode<T>();
    node->data=x;
    node->next=headnode;
    headnode=node;
}

template<class T>
void main()
{
	cout << "hello world----" << endl;
	myslist<T> *objMylist;
	objMylist->add("tail");
	objMylist->insertHead("head");
}