using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnMouseDown_Hide : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnMouseDown()              // ��ġ�ϸ�
    {
        this.gameObject.SetActive(false);   // �����
    }
}
